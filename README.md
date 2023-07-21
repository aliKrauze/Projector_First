# Projector_First
100 cats

The algorithm:

1. Set an array including all the cats, but without hats
2. Start a loop with 100 rounds. With each round walk through a circle and put a hat on a cat based on a round number
3. Print indexes of the cats that have hats.

The pseudo-code

Function calculate_hats(num_cats, num_rounds):
  Set an array of num_cats, including cats without hats
  
  For round in range from 1 to num_rounds:
     For catIndex in range from round to num_cats:
        Set the hat status of cat at catIndex

  Set an empty list to store the indexes of cats with hats

  For catIndex in range from 1 to num_cats:
    If the at catIndex has a hat:
      Add catIndex to the list of cats with hats

  Return the list of cats with hats

  Print  result
