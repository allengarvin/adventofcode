package main

import(
    "bufio"
    "fmt"
    "os"
    "strconv"
)

func read_file(fn string) []int {
    fd, err := os.Open(fn)
    if err != nil {
        fmt.Fprintf(os.Stderr, "%s: unable to read", fn)
        os.Exit(1)
    }

    var lines []int
    scanner := bufio.NewScanner(fd)
    for scanner.Scan() {
        n, _ := strconv.Atoi(scanner.Text())
        lines = append(lines, n)
    }
    return lines
}

func comb2(numbers []int) int {
    for _, m := range numbers {
        for _, n := range numbers {
            if m + n == 2020 {
                return m * n
            }
        }
    }
    return -1
}


func comb3(numbers []int) int {
    for _, m := range numbers {
        for _, n := range numbers {
            for _, o := range numbers {
                if m + n + o== 2020 {
                    return m * n * o
                }
            }
        }
    }
    return -1
}

func main() {
    numbers := []int{}

    numbers = read_file("01-input.txt")

    fmt.Printf("Part 1: %d\n", comb2(numbers))
    fmt.Printf("Part 2: %d\n", comb3(numbers))
}
    
