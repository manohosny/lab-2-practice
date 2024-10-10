# User Registration Application

This is a simple user registration web application built with Python and Flask. The application allows users to register by providing their name, email, gender, and country. Registered users are displayed in a list on a separate page.

## Features

- User registration form
- Input validation for name, email, gender, and country
- View a list of all registered users
- Simple error handling for invalid submissions

## File Structure

- `app.py`: The main Flask application file that handles routes and backend logic.
- `templates/`
  - `index.html`: The registration page where users can fill out the form.
  - `users.html`: The page displaying all registered users.
- `static/css/`
  - `style.css`: The stylesheet containing styles for the application.
  
## How to Run the Application

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install the dependencies**:
   Ensure you have Python and Flask installed. You can install Flask via pip:
   ```bash
   pip install Flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   Open your browser and go to `http://127.0.0.1:5000` to access the user registration page.

## HTML Templates

- `index.html`:
  - Contains the registration form for users to fill out their details.
  - Includes a link to the users' list page.

- `users.html`:
  - Displays a table of all registered users with their name, email, gender, and country.

## CSS Styling

The application's CSS is stored in `static/css/style.css` and includes styling for the form, buttons, and table elements. Key classes used include:
- `.form-group`: Styles for form labels and input fields.
- `.btn`: Base class for buttons, with additional styling for `.btn-primary`.
- `.container`: A container class to center and add padding to the content.

## Example Pages

- **Registration Page**:
  ![Registration Page](images/registration.png)

- **Users List Page**:
  ![Users List Page](images/users_list.png)

## Future Improvements

- Add authentication and user login functionality.
- Implement database storage for user data (currently, data is stored in-memory).
- Add form validation and error messaging for specific invalid inputs.

## License

This project is licensed under the MIT License.
```
