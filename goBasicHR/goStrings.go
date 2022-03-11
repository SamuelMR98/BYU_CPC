package main

import (
    "bufio"
    "fmt"
    "io"
    "os"
    "strings"
)

/*
 * Complete the 'ModifyString' function below and add imports if needed.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING str as parameter.
 */

 func reverse(s string) string {
    rns := []rune(s) 
    for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {
        rns[i], rns[j] = rns[j], rns[i]
    }
    return string(rns)
}

func ModifyString(str string) string {
	s := strings.ReplaceAll(str, " ", "");
	s := s.replace(/[0-9]/g, "");
	s := reverse(s);

	return s
}

func main() {
    reader := bufio.NewReaderSize(os.Stdin, 16 * 1024 * 1024)

    stdout, err := os.Create(os.Getenv("OUTPUT_PATH"))
    checkError(err)

    defer stdout.Close()

    writer := bufio.NewWriterSize(stdout, 16 * 1024 * 1024)

    str := readLine(reader)

    result := ModifyString(str)

    fmt.Fprintf(writer, "%s\n", result)

    writer.Flush()
}

func readLine(reader *bufio.Reader) string {
    str, _, err := reader.ReadLine()
    if err == io.EOF {
        return ""
    }

    return strings.TrimRight(string(str), "\r\n")
}

func checkError(err error) {
    if err != nil {
        panic(err)
    }
}