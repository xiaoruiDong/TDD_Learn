from selenium import webdriver
browser = webdriver.Firefox()

# we have a new website launched online and we will visit it right now
browser.get('http://localhost:8000')

# we will notice that there is To-Do in both of the title and the head
assert 'To-Do' in browser.title

# Then we will make a to-do list

# we first type "Buy peacock feathers" in the text box

# after pressing enter, the webpage is refreshed with '1: Buy peacock feathers'

# And at the time, another text box popped out

# We input "Use peacock feathers to make a fly"

# Webpage refreshed again and showed these 2 To-Do

# We want to know if the To-Do is saved

# We will noticed that we are now having our exclusive URL

# When we visit that url, the list is still there

# we shut down the webdriver with satisfaction

browser.quit()