#!/usr/bin/env python3
"""Friday Warmup | Returning Data From Complex JSON"""

import requests
import html
URL= "https://opentdb.com/api.php?amount=10&category=27&difficulty=medium&type=multiple"
#https://opentdb.com/api_config.php
def main():
    
    # data will be a python dictionary rendered from your API link's JSON!
    data= requests.get(URL).json()
    
#    response = json.load(data)
    for result in data["results"]:
       questions = html.unescape(result["question"])
       correct_ans = html.unescape(result["correct_answer"])
       print(questions)
       print(correct_ans)
    
if __name__ == "__main__":
    main()
