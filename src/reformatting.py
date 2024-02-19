from bs4 import BeautifulSoup
import logging
import json

def html_extract(json_result):
    """
    Extracts and orders the contents from the HTML data within the provided JSON result.

    Parameters:
    json_result (dict): The JSON result from the Watson Discovery service.

    Returns:
    list: The ordered contents extracted from the HTML.
    """
    if not json_result.get('results'):
        raise ValueError('No results found in the provided JSON result.')
    
    html_data = json_result['results'][0]['html']
    soup = BeautifulSoup(html_data, 'html.parser')

    contents_ordered = []  # Initialize an empty list to store the ordered contents

    for bbox in soup.find_all('bbox'):
        parent_span = bbox.find_parent('span')
        if parent_span and 'class' in parent_span.attrs and parent_span['class']:
            class_name = parent_span['class'][0] if parent_span['class'] else 'unknown'
            
            if class_name in ['title', 'text', 'subtitle', 'subsubtitle', 'Head', 'table']:
                content_text = bbox.get_text(strip=True)
                contents_ordered.append({class_name: content_text})
    return contents_ordered

def reformat_contents(contents_ordered):
    sections = []  # Stores the final structured sections
    context = {'title': '', 'subtitle': '', 'subsubtitle': '', 'Head': ''}  # Initialize context without 'text'
    current_text = ''  # Store current text separately

    hierarchy = {'title': 1, 'subtitle': 2, 'subsubtitle': 3, 'Head': 4}  # 'text' is not part of hierarchy
    current_level = 0  # Track the current hierarchy level

    for content in contents_ordered:
        if isinstance(content, dict):  # Ensure content is a dictionary
            key, value = next(iter(content.items()))

            if key in hierarchy:
                content_level = hierarchy[key]
                if content_level <= current_level:
                    # If there's any text, append the current section before starting a new one
                    if current_text:
                        sections.append({**context, 'text': current_text})
                        current_text = ''  # Reset current text

                    # Reset context for lower levels
                    for lower_key in hierarchy:
                        if hierarchy[lower_key] >= content_level:
                            context[lower_key] = ''
                            
                # Update the context with the new value
                context[key] = value
                current_level = content_level  # Update the current level

            elif key == 'text':
                # Append current text if it belongs to the same context
                current_text += (' ' + value if current_text else value)

        else:
            logging.error(f"Unexpected format: {content}")

    # Add the last section if there's any text left
    if current_text:
        sections.append({**context, 'text': current_text})

    return sections

def elastic_search_formatting(formatted_results, index_name):
    transformed_data = []
    for item in formatted_results:
        index_metadata = {"index": {"_index": index_name}}
        transformed_data.append(index_metadata)
        transformed_data.append(item)
    ndjson_formatted_documents = '\n'.join(json.dumps(doc) for doc in transformed_data) + '\n'
    return ndjson_formatted_documents