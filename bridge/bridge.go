package main

import (
	"fmt"
	"log"
	"time"
)

func main() {
	log.Println("Starting IBKR Bridge stub…")
	for {
		time.Sleep(10 * time.Second)
		fmt.Println("Polling for IBKROrderRequested events…")
		fmt.Println("Placing order on IBKR for SPY, 100 shares @ 410.00")
		fmt.Println("Order placed. (Proof stub)")
	}
}