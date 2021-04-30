### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: # need to be equate(==) sign here 
      return True
    else              # next to else is colon (:) required
      return False
   

  dif highest_card(self, card1 card2): # spelling mistake of def
  if card1.value > card2.value:
    return card       # there is no card object here, needs to be card1
  else:
    return card2
  


def cards_total(self, cards):
  total            # total is not assigned any value here, so when doing total += card.value the total will be un assigned and cant be computed
  for card in cards:
    total += card.value
    return "You have a total of" + total  # cant concatenate string and integer need to convert total into string first before concatination
  
```
