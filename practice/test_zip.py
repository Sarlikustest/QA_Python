test_scores = [75, 90, 85, 60, 95]
prog_scores = [80, 70 ,90, 75, 75]
zip_scores = list(zip(test_scores, prog_scores))
for i, j in zip_scores:
    if i > 80 and j > 80:
        print(i, j)