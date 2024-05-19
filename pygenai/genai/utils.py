def find_citations(data):
    citations = []

    for item in data:
        response_text = item.get('response', '')
        sources = item.get('sources', [])
        cited_sources = []

        for source in sources:
            if source.get('context', '') in response_text:
                cited_sources.append({
                    'id': source['id'],
                    'link': source.get('link', '')
                })

        citations.append(cited_sources)

    return citations
