
def main():
  mylist=build_request(catalog)
  print(" ")
  request_subtotal=calculate_subtotal(mylist,catalog)

  total=shipping_and_overhead(request_subtotal)
  return total
  #this fuction gathers all the functions together. Using functions was easier than a long code because when I was
  #having difficulty figuring how why something was not working I only had to focus on one area because I was able to successfully
  #run the others. So then I knew where my problem was. I did have difficulty with the main() function when making sure I was passing
  #the correct thing, but I figured out that I needed to assign the functions a name and then pass it through to the next function.
