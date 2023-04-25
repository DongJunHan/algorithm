package main
import "fmt"
func main(){
    var input int
    count := 0
    fmt.Scanln(&input)
    for i := 1; i <= input; i++{
        if i / 100 != 0{
            first := i / 100
            second := (i % 100) / 10
            third := (i % 100) % 10
            if(second - first) == (third - second) {
                count++
            }
        }else{
            count++
        }
    }
    fmt.Println(count)
}