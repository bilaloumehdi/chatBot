# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from services.weather import get_weather

class ActionWeather(Action):

    def name(self) -> Text:
        return "action_forecast_weather"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = next(tracker.get_latest_entity_values('city'),None)

        if not city:
            dispatcher.utter_message(text="sorry, no city detected, you need to specify me the city in your message")
        
        temp , place, desc = get_weather(city)

        if not temp:
            dispatcher.utter_message(text='I could not get the the weather info. maybe it is a spelling error')

        msg = f"currently it is {temp} °C in {place}. It's a {desc} day"
        dispatcher.utter_message(text=msg)
        
        return []
