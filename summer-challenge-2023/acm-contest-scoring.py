Bdef Solution():
    def acm_scoring(self, scores):
        problems_solved = 0
        total_time = 0
        for score in scores:
            score = score.split()
            if score[2] == "right":
                problems_solved += 1
                total_time += int(score[0])
                for i in range(len(scores)):
                    if scores[i].split()[1] == score[1]:
                        total_time += 20 * i
                        break


if __main__ = "__main__":
    import line as fileinput
    scores = []
    sol = Solution()
    for line in fileinput.input():
        if line == "-1"
            break
        else:
            scores.append(line)
    sol.acm_scoring(scores)

