def calc_hats(num_cats, num_rounds):
    cats = [False] * num_cats

    for round in range(1, num_rounds + 1):
        for cat_index in range(round, num_cats + 1, round):
            cats[cat_index - 1] = not cats[cat_index - 1]
    
    cats_with_hats = [index + 1 for index, has_hat in enumerate(cats) if has_hat]
    return cats_with_hats

hats_at_end = calc_hats(100, 100)
print(f"Cats wearing hats at the end: {hats_at_end}")