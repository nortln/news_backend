# News Backend Application

A Django-based news portal application with features like infinite scroll, news tagging, like functionality, and view statistics.

## Features

- **News Management**
  - Create, read, update, and delete news articles
  - Add tags to news articles
  - Upload images for news articles
  - View count tracking

- **User Interaction**
  - Like functionality (IP-based)
  - Infinite scroll for news listing
  - View news by specific tags

- **Statistics**
  - Most viewed news
  - Most liked news

- **Admin Panel**
  - Manage news articles
  - Manage tags
  - View likes and statistics

## Setup Instructions

### Prerequisites
- Python 3.8+
- Django 5.0+
- SQLite (or any other Django-supported database)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/news_backend.git
   cd news_backend
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

### Configuration

1. Media files:
   - Create a `media` directory in the project root
   - Add the following to `settings.py`:
     ```python
     MEDIA_URL = '/media/'
     MEDIA_ROOT = BASE_DIR / 'media'
     ```

2. Static files:
   - Run `python manage.py collectstatic` in production

### Usage

#### Endpoints

- **News List**: `/news/`
- **News Detail**: `/news/<int:pk>/`
- **News by Tag**: `/news/tag/<str:tag>/`
- **Statistics**: `/news/statistics/`
- **Like News**: `/news/<int:pk>/like/` (POST)

#### Admin Panel

Access the admin panel at `/admin/` using your superuser credentials to:
- Manage news articles
- Manage tags
- View likes and statistics

#### Infinite Scroll

The news list page implements infinite scroll:
- Loads 3 news items at a time
- Automatically loads more when scrolling to the bottom
- Maintains consistent image dimensions (50% width, 200px height)

#### Image Handling

- News images are stored in `media/news_images/`
- All images are displayed with:
  - 50% width
  - 200px height
  - `object-fit: cover` to maintain aspect ratio
  - Rounded corners

## Technology Stack

- **Backend**: Django
- **Database**: SQLite (default)
- **Frontend**: Bootstrap 5
- **JavaScript**: jQuery for AJAX requests

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [your-email@example.com](mailto:clintontristanacje@gmail.com) 
