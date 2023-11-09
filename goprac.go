
import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: go run squares.go <integer>")
		return
	}

	// Parse the command line argument to an integer
	maxNum, err := strconv.Atoi(os.Args[1])
	if err != nil {
		fmt.Printf("Error: '%s' is not a valid integer.\n", os.Args[1])
		return
	}

	fmt.Printf("Perfect squares up to %d are:\n", maxNum)
	for i := 1; i*i <= maxNum; i++ {
		fmt.Println(i * i)
	}
}
