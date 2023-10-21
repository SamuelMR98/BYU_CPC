# Input: a sequence of up to 2000 commands, one per line, ending at EOF. Each command is either a definition, a calculation or a clear.
# Output: For each calculation command, print the result of the calculation or unknown if the calculation is impossible to determine.


class Solution:
    words = {}
    other = {}
    
    def parse(self, command):
        command = command.split()
        if command[0] == "def":
            self.words[command[1]] = int(command[2])
        elif command[0] == "calc":
            result = 0
            sign = 1
            for i in range(1, len(command) - 1):
                if command[i] == "+":
                    sign = 1
                elif command[i] == "-":
                    sign = -1
                elif command[i] == "=":
                    if result in self.words.values():
                        for key, value in self.words.items():
                            if value == result:
                                print(" ".join(command[1:]) + " " + key)
                                return
                    else:
                        print(" ".join(command[1:]) + " " + "unknown")
                        return
                else:
                    if command[i] in self.words:
                        result += sign * self.words[command[i]]
                    else:
                        print(" ".join(command[1:]) + " " + "unknown")
                        return
        elif command[0] == "clear":
            self.words = {}
        else:
            print(" ".join(command[1:]) + " " + "unknown")
            return

        
        

        

if __name__ == "__main__":
    import fileinput
    sol = Solution()
    for line in fileinput.input():
        sol.parse(line)
    


    