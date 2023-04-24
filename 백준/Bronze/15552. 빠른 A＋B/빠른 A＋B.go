package main
import (
    "fmt"
    "bufio"
    "os"
)
func main(){
    var input1,input2,total int
    reader := bufio.NewReader(os.Stdin)
    writer := bufio.NewWriter(os.Stdout)
    fmt.Scan(&total)
    for i := 1; i <= total; i++{
        fmt.Fscanln(reader,&input1,&input2)
        fmt.Fprintln(writer, input1 + input2)
    }
    writer.Flush()
}