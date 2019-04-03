from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import csv

# Specifying incognito mode as you launch your browser[OPTIONAL]

header = ["Team","Name","Played","Goals","Assists","Rating"]
with open('test.csv','w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
csvfile.close()
# Go to desired website
teams = ["https://www.whoscored.com/Teams/26/Show/England-Liverpool","https://www.whoscored.com/Teams/13/Show/England-Arsenal","https://www.whoscored.com/Teams/167/Show/England-Manchester-City","https://www.whoscored.com/Teams/32/Show/England-Manchester-United","https://www.whoscored.com/Teams/15/Show/England-Chelsea","https://www.whoscored.com/Teams/30/Show/England-Tottenham","https://www.whoscored.com/Teams/161/Show/England-Wolverhampton-Wanderers","https://www.whoscored.com/Teams/27/Show/England-Watford","https://www.whoscored.com/Teams/29/Show/England-West-Ham","https://www.whoscored.com/Teams/14/Show/England-Leicester","https://www.whoscored.com/Teams/31/Show/England-Everton","https://www.whoscored.com/Teams/183/Show/England-Bournemouth","https://www.whoscored.com/Teams/23/Show/England-Newcastle-United","https://www.whoscored.com/Teams/162/Show/England-Crystal-Palace","https://www.whoscored.com/Teams/211/Show/England-Brighton","https://www.whoscored.com/Teams/18/Show/England-Southampton","https://www.whoscored.com/Teams/184/Show/England-Burnley","https://www.whoscored.com/Teams/188/Show/Wales-Cardiff","https://www.whoscored.com/Teams/170/Show/England-Fulham","https://www.whoscored.com/Teams/166/Show/England-Huddersfield"]

# teamname_element = [None]*(len(teams)+1)
# title_element =[None]*(len(teams)+1)
# title=[None]*(len(teams)+1)
# goals_element=[None]*(len(teams)+1)
# goals=[None]*(len(teams)+1)
# assists_element=[None]*(len(teams)+1)
# assists=[None]*(len(teams)+1)
# rating_element=[None]*(len(teams)+1)
# rating=[None]*(len(teams)+1)
# teamname=[None]*(len(teams)+1)
# team=[None]*(len(teams)+1)

i=0
while (i<len(teams)):
    # Create new Instance of Chrome in incognito mode
    option = webdriver.ChromeOptions()
    browser = webdriver.Chrome(executable_path='/Users/aryamanpratapsingh/Desktop/py/chromedriver', chrome_options=option)
    browser.get(teams[i])

    # Wait 20 seconds for page to load
    timeout = 200
    try:
        # Wait until the final element [Avatar link] is loaded.
        # Assumption: If Avatar link is loaded, the whole page would be relatively loaded because it is among
        # the last things to be loaded.
        WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='team-formations-content']")))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()

    # Get all of the titles for the pinned repositories
    # We are not just getting pure titles but we are getting a selenium object
    # with selenium elements of the titles.

    # find_elements_by_xpath - Returns an array of selenium objects.
    # teamname_element[i] = browser.find_element_by_xpath(".//*[@id='layout-content-wrapper']/div[2]/div[1]/h2/span")
    #
    # title_element[i] = browser.find_elements_by_xpath(".//*[@id='player-table-statistics-body']/tr/td[3]")
    # # List Comprehension to get the actual repo titles and not the selenium objects.
    # title[i] = [x.text for x in title_element[i]]
    # goals_element[i] = browser.find_elements_by_xpath(".//*[@id='player-table-statistics-body']/tr/td[8]")
    # goals[i] = [x.text for x in goals_element[i]]
    # assists_element[i] = browser.find_elements_by_xpath(".//*[@id='player-table-statistics-body']/tr/td[9]")
    # assists[i] = [x.text for x in assists_element[i]]
    # rating_element[i] = browser.find_elements_by_xpath(".//*[@id='player-table-statistics-body']/tr/td[16]")
    # rating[i] = [x.text for x in rating_element[i]]
    #
    # teamname[i] = [teamname_element[i].text]*len(title[i])
    # # print response in terminal
    # team[i] = list(zip(teamname[i],title[i],goals[i],assists[i],rating[i]))
    # print(team[i])

    teamname_element = browser.find_element_by_xpath(".//*[@id='layout-content-wrapper']/div[2]/div[1]/h2/span")

    title_element = browser.find_elements_by_xpath(".//*[@id='player-table-statistics-body']/tr/td[3]")
    # List Comprehension to get the actual repo titles and not the selenium objects.
    title = [x.text for x in title_element]
    goals_element = browser.find_elements_by_xpath(".//*[@id='player-table-statistics-body']/tr/td[8]")
    goals = [x.text for x in goals_element]
    assists_element = browser.find_elements_by_xpath(".//*[@id='player-table-statistics-body']/tr/td[9]")
    assists = [x.text for x in assists_element]
    rating_element = browser.find_elements_by_xpath(".//*[@id='player-table-statistics-body']/tr/td[16]")
    rating = [x.text for x in rating_element]
    played_element = browser.find_elements_by_xpath("//*[@id='player-table-statistics-body']/tr/td[6]")
    playedraw = [x.text for x in played_element]
    #Splitting values of form Int(Int) to only store initial integer
    played = []
    for p in playedraw:
        psplit = p.split("(")
        played.append(psplit[0])
    #Clicking link to change tab
    detailed_view = browser.find_element_by_xpath("//*[@id='team-squad-stats-options']/li[5]/a")
    detailed_view.click()
    key_passes = browser.find_element_by_xpath("//*[@id='category']/optgroup[3]/option[2]")
    key_passes.click()
    select_type = browser.find_element_by_xpath("//*[@id='subcategory']/option[2]")
    select_type.click()
    crosspg_element = browser.find_elements_by_xpath("//*[@id='player-table-statistics-body']/tr/td[8]")
    cross_pg = [x.text for x in crosspg_element]
    throughball_pg_element = browser.find_elements_by_xpath("//*[@id='player-table-statistics-body']/tr/td[9]")
    throughball_pg = [x.text for x in throughball_pg_element]
    teamname = [teamname_element.text]*len(title)
    # print response in terminal
    team = list(zip(teamname,title,played,goals,assists,rating))
    print(team)

    #Write to CSV file

    with open('test.csv','a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(team)
        print("writing ")
        print(str(i))
    csvfile.close()

    browser.close()
    i = i+1

# Get all of the pinned repo languages
#language_element = browser.find_elements_by_xpath("//p[@class='mb-0 f6 text-gray']")
#languages = [x.text for x in language_element] # same concept as for-loop/ list-comprehension above.

# print response in terminal
#print("LANGUAGES:")
#print(languages, '\n')

# Pair each title with its corresponding language using zip function and print each pair
#for title, language in zip(titles, languages):
 #   print("RepoName : Language")
  #  print(title + ": " + language, '\n')



