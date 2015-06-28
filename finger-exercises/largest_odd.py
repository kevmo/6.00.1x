def biggest_odd(numbers):
  """Return the largest odd number.

  :param numbers: Array of numbers.
  """
  largest = None

  for num in numbers:
    if num % 2 is 0:
      continue
    else:
      if num > largest:
        largest = num

  return largest


# Tests

none = []
print "This should be None:", biggest_odd(none)

no_odds = [10, 2, 4, 6, 8]
print "This should be None:", biggest_odd(no_odds)

evens_and_odds = [69, 102, 169, 2, 12, 5]
print "This should be 169:", biggest_odd(evens_and_odds)
