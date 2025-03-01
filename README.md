# Password Generator  
[Watch the demo]
. This Python script generates secure passwords based on user preferences. It allows users to customize password length, include uppercase letters, special characters, and specify the number of passwords to generate.  

## Features  
- Generate passwords with a specified length  
- Option to include uppercase letters  
- Option to include special characters  
- Generate multiple passwords at once  

## How It Works  
1. The script prompts the user to enter the desired password length.  
2. The user is asked whether they want to include uppercase letters.  
3. The user is asked whether they want to include special characters.  
4. The user specifies the number of passwords to generate.  
5. The script generates the passwords using a combination of lowercase letters, uppercase letters (if selected), and special characters (if selected).  
6. The generated passwords are displayed on the screen.  

## Usage  
Run the script and follow the prompts to generate customized passwords.  

## Requirements  
- Python 3.x  
- No additional libraries required (uses built-in modules: `random` and `string`)  

## Example Output  
```
How many characters should your password be?(1, 2 ,3...) >> 12  
Should your password contain uppercase letters?(y/n) >> y  
Should your password contain special characters?(y/n) >> y  
How many passwords would you like to generate?(1, 2 ,3...) >> 3  

Here are your passwords:  
A3d@fG#1sK9p  
m!Z7qR2xL8oV  
p$H6yT4wJ5uN  
```  

This script provides an easy and interactive way to generate secure passwords based on user preferences.
