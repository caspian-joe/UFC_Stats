from parsel import Selector
import requests
import time
import random

def wait_random_time():
    wait_time = random.randint(2, 5)
    print(f"Waiting for {wait_time} seconds...")
    time.sleep(wait_time)

def get_fights_records(response, headers, number_of_events = 1):
    fights = get_fights(response, headers, number_of_events)
    ufc_fight_records = []

    for fight in fights:
        wait_random_time()
        url = fight['link']
        selector = Selector(requests.get(url, headers=headers).text)
        for rounds in range(int(fight['total_rounds'])):
            table_row = 2 * rounds + 2
            for records in selector.css('div.b-fight-details'):
                ufc_fight_records_A = {
                    'event_name': fight['event_name'],
                    'fight_name': fight['fight_name'],
                    'weight_class': fight['weight_class'],
                    'winning_method': fight['method'],
                    'total_rounds': fight['total_rounds'],
                    'time': fight['time'],
                    'link': fight['link'],
                    'fighter_name': None,
                    'opponent_name': None,
                    'win/loss': None,
                    'round': None,
                    'Knock_Down': None,
                    'Take_Down': None,
                    'Submission_Attempt': None,
                    'Reversal': None,
                    'Control_Time': None,
                    'Head': None,
                    'Body': None,
                    'Leg': None,
                    'Distance': None,
                    'Clinch': None,
                    'Ground': None,
                }

                ufc_fight_records_B = {
                    'event_name': fight['event_name'],
                    'fight_name': fight['fight_name'],
                    'weight_class': fight['weight_class'],
                    'winning_method': fight['method'],
                    'total_rounds': fight['total_rounds'],
                    'time': fight['time'],
                    'link': fight['link'],
                    'fighter_name': None,
                    'opponent_name': None,
                    'win/loss': None,
                    'round': None,
                    'Knock_Down': None,
                    'Take_Down': None,
                    'Submission_Attempt': None,
                    'Reversal': None,
                    'Control_Time': None,
                    'Head': None,
                    'Body': None,
                    'Leg': None,
                    'Distance': None,
                    'Clinch': None,
                    'Ground': None,
                }
                try:
                    ufc_fight_records_A['fighter_name'] = records.css('div.b-fight-details__persons.clearfix > div:nth-child(1) > div > h3 > a::text').get().strip()
                    ufc_fight_records_A['opponent_name'] = records.css('div.b-fight-details__persons.clearfix > div:nth-child(2) > div > h3 > a::text').get().strip()
                    ufc_fight_records_A['win/loss'] = records.css('div.b-fight-details__persons.clearfix > div:nth-child(1) > i::text').get().strip()
                    ufc_fight_records_A['round'] = rounds + 1
                    ufc_fight_records_A['Knock_Down'] = records.css(f'section:nth-child(5) > table > tbody > tr:nth-child({table_row})> td:nth-child(2) > p:nth-child(1)::text').get().strip()
                    ufc_fight_records_A['Take_Down'] = records.css(f'section:nth-child(5) > table > tbody > tr:nth-child({table_row})> td:nth-child(6) > p:nth-child(1)::text').get().strip()
                    ufc_fight_records_A['Submission_Attempt'] = records.css(f'section:nth-child(5) > table > tbody > tr:nth-child({table_row})> td:nth-child(8) > p:nth-child(1)::text').get().strip()
                    ufc_fight_records_A['Reversal'] = records.css(f'section:nth-child(5) > table > tbody > tr:nth-child({table_row})> td:nth-child(9) > p:nth-child(1)::text').get().strip()
                    ufc_fight_records_A['Control_Time'] = records.css(f'section:nth-child(5) > table > tbody > tr:nth-child({table_row})> td:nth-child(10) > p:nth-child(1)::text').get().strip()
                    ufc_fight_records_A['Head'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(4) > p:nth-child(1)::text').get().strip()
                    ufc_fight_records_A['Body'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(5) > p:nth-child(1)::text').get().strip()
                    ufc_fight_records_A['Leg'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(6) > p:nth-child(1)::text').get().strip()
                    ufc_fight_records_A['Distance'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(7) > p:nth-child(1)::text').get().strip()
                    ufc_fight_records_A['Clinch'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(8) > p:nth-child(1)::text').get().strip()
                    ufc_fight_records_A['Ground'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(9) > p:nth-child(1)::text').get().strip()

                    ufc_fight_records_B['fighter_name'] = records.css('div.b-fight-details__persons.clearfix > div:nth-child(2) > div > h3 > a::text').get().strip()
                    ufc_fight_records_B['opponent_name'] = records.css('div.b-fight-details__persons.clearfix > div:nth-child(1) > div > h3 > a::text').get().strip()
                    ufc_fight_records_B['win/loss'] = records.css('div.b-fight-details__persons.clearfix > div:nth-child(2) > i::text').get().strip()
                    ufc_fight_records_B['round'] = rounds + 1
                    ufc_fight_records_B['Knock_Down'] = records.css(f'section:nth-child(5) > table > tbody > tr:nth-child({table_row})> td:nth-child(2) > p:nth-child(2)::text').get().strip()
                    ufc_fight_records_B['Take_Down'] = records.css(f'section:nth-child(5) > table > tbody > tr:nth-child({table_row})> td:nth-child(6) > p:nth-child(2)::text').get().strip()
                    ufc_fight_records_B['Submission_Attempt'] = records.css(f'section:nth-child(5) > table > tbody > tr:nth-child({table_row})> td:nth-child(8) > p:nth-child(2)::text').get().strip()
                    ufc_fight_records_B['Reversal'] = records.css(f'section:nth-child(5) > table > tbody > tr:nth-child({table_row})> td:nth-child(9) > p:nth-child(2)::text').get().strip()
                    ufc_fight_records_B['Control_Time'] = records.css(f'section:nth-child(5) > table > tbody > tr:nth-child({table_row})> td:nth-child(10) > p:nth-child(2)::text').get().strip()
                    ufc_fight_records_B['Head'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(4) > p:nth-child(2)::text').get().strip()
                    ufc_fight_records_B['Body'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(5) > p:nth-child(2)::text').get().strip()
                    ufc_fight_records_B['Leg'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(6) > p:nth-child(2)::text').get().strip()
                    ufc_fight_records_B['Distance'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(7) > p:nth-child(2)::text').get().strip()
                    ufc_fight_records_B['Clinch'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(8) > p:nth-child(2)::text').get().strip()
                    ufc_fight_records_B['Ground'] = records.css(f'section:nth-child(8) > table > tbody > tr:nth-child({table_row})> td:nth-child(9) > p:nth-child(2)::text').get().strip()

                    ufc_fight_records.append(ufc_fight_records_A)
                    ufc_fight_records.append(ufc_fight_records_B)

                except:
                    pass

    return ufc_fight_records



def get_fights(response, headers, number_of_events = 1):
    events = get_events(response)
    if number_of_events == 'all':
        n = int(len(events))
    else:
        n = number_of_events
    ufc_fights = []
    
    for event in events[:n]:
        url = event['link']
        event_name = event['name']
        selector = Selector(requests.get(url, headers=headers).text)

        for fights in selector.css('tr.b-fight-details__table-row')[1:]:

            fight = {
                'event_name': None,
                'fight_name': None,
                'weight_class': None,
                'method': None,
                'total_rounds': None,
                'time': None,
                'link': None
            }
            try:
                fight['event_name'] = event_name
                fighter1 = fights.css('td:nth-child(2) > p:nth-child(1) > a::text').get().strip()
                fighter2 = fights.css('td:nth-child(2) > p:nth-child(2) > a::text').get().strip()
                fight['fight_name'] = fighter1 + ' vs ' + fighter2
                fight['weight_class'] = fights.css('td:nth-child(7) > p::text').get().strip()
                fight['method'] = fights.css('td:nth-child(8) > p:nth-child(1)::text').get().strip()
                fight['total_rounds'] = fights.css('td:nth-child(9) > p::text').get().strip()
                fight['time'] = fights.css('td:nth-child(10) > p::text').get().strip()
                fight['link'] = fights.css('td > p > a').attrib['href']

                ufc_fights.append(fight)

            except:
                pass

    return ufc_fights



def get_events(response):
    selector = Selector(text = response.text)
    
    ufc_events = []
    for events in selector.css('tr.b-statistics__table-row'):
        event = {
            'name': None,
            'date': None,
            'location': None,
            'link': None,
        }

        try:
            event['name'] = events.css('a.b-link_style_black::text').get().strip()
            event['date'] = events.css('span.b-statistics__date::text').get().strip()
            event['location'] =  events.css('td.b-statistics__table-col_style_big-top-padding::text').get().strip()
            event['link'] =  events.css('a.b-link_style_black').attrib['href']

            ufc_events.append(event)

        except:
            pass

    return ufc_events

