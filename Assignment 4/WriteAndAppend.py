user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n")

    # Step 2: Append to file
additional_input = input("Enter additional text to append to the file: ")
with open("output.txt", "a") as file:
    file.write(additional_input + "\n")

    # Step 3: Read and display the final content
print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    file_content = file.read()
    print(file_content)
file.close()