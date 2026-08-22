#!/bin/bash

while true
do
    echo "Calculator"
    echo "1. Add"
    echo "2. Subtract"
    echo "3. Multiply"
    echo "4. Divide"
    echo "5. Exit"

    read -p "Enter your choice: " choice

    if [ $choice -eq 5 ]
    then
        echo "Goodbye"
        break
    fi

    read -p "Enter first number: " a
    read -p "Enter second number: " b

    if [ $choice -eq 1 ]
    then
        echo "Answer: $((a + b))"

    elif [ $choice -eq 2 ]
    then
        echo "Answer: $((a - b))"

    elif [ $choice -eq 3 ]
    then
        echo "Answer: $((a * b))"

    elif [ $choice -eq 4 ]
    then
        if [ $b -eq 0 ]
        then
            echo "Cannot divide by zero"
        else
            echo "Answer: $((a / b))"
        fi

    else
        echo "Invalid choice"
    fi

    echo ""
done