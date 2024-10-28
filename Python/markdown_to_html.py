def markdown_to_html(markdown):
    return markdown.replace('# ', '<h1>').replace('#', '</h1>')
