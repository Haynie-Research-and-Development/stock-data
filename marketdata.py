#!/usr/local/bin/python3.8
#**********************************************************
#* CATEGORY	SOFTWARE
#* GROUP	MARKET DATA
#* AUTHOR	LANCE HAYNIE <LANCE@HAYNIEMAIL.COM>
#* DATE		2020-08-20
#* PURPOSE	ETL MARKET DATA INTO MYSQL TABLES
#* FILE		MARKETDATA.PY
#**********************************************************
#* MODIFICATIONS
#* 2020-08-20 - LHAYNIE - INITIAL VERSION
#**********************************************************
#ETL Stock Market Data
#Copyright 2020 Haynie IPHC, LLC
#Developed by Haynie Research & Development, LLC
#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.#
#You may obtain a copy of the License at
#http://www.apache.org/licenses/LICENSE-2.0
#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.
import sys

if sys.argv[1] == None:
    print("No option provided, use --help for options.")
else:
    if sys.argv[1].lower() == "--help":
        print("help stuff")
    elif sys.argv[1].lower() == "--exchange":
        if sys.argv[2].lower() == "nyse":
            import marketdata.symbol
            marketdata.symbol.update(marketdata.symbol.nyse())
        elif sys.argv[2].lower() == "nasdaq":
            import marketdata.symbol
            marketdata.symbol.update(marketdata.symbol.nasdaq())
        else:
            print("Error: unrecognized exchange code.")
    elif sys.argv[1].lower() == "--overview":
        import marketdata.overview
        marketdata.overview.update()
    elif sys.argv[1].lower() == "--daily":
        import marketdata.daily
        marketdata.daily.update()
    elif sys.argv[1].lower() == "--technical":
        import marketdata.technical
        marketdata.technical.update()
    elif sys.argv[1].lower() == "--check_config":
        print("Just making sure everything works!")
    else:
        print("Error: invalid option, use --help for options.")
exit(0)
