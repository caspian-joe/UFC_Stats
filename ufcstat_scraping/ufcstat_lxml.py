from lxml import html

def get_events(response):
    tree = html.fromstring(response.content)

    events_tbl = tree.xpath('/html/body/section/div/div/div/div[2]/div/table/tbody')[0]
    trs = events_tbl.xpath('.//tr')

    ufc_events = []

    for tr in trs[1:]:
        ufc_event = {
            'name': None,
            'date': None,
            'location': None,
            'link': None
        }
        ufc_event['name'] = tr.xpath('td[1]/i/a/text()')[0].strip()
        ufc_event['date'] = tr.xpath('td[1]/i/span')[0].text.strip()
        ufc_event['link'] = tr.xpath('td[1]/i/a/@href')[0].strip()
        ufc_event['location'] = tr.xpath('td[2]/text()')[0].strip()
        ufc_events.append(ufc_event)

    return ufc_events
