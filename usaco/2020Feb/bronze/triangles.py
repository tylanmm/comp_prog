with open("triangles.in") as f:
    n = int(f.readline().strip())
    posts = [tuple(map(int, f.readline().split())) for i in range(n)]

# Since there's 100 posts max, just use each post as the right angle
# vertex of the triangle and see what two points make the largest
# base and height with that vertex
maxA = 0
for p in posts:
    maxB = 0
    maxH = 0
    for i in range(len(posts)):
        if posts[i][0] == p[0]:
            maxH = max(maxH, abs(p[1] - posts[i][1]))
        if posts[i][1] == p[1]:
            maxB = max(maxB, abs(p[0] - posts[i][0]))
    maxA = max(maxA, maxB * maxH)

with open("triangles.out", "w") as f:
    f.write(str(maxA) + "\n")