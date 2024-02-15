 My Django Project

My Django project is a web application designed to demonstrate the Dynamic Pricing of delivery cost.

## Prerequisites

- Python  3.x
- Django  3.1.14
- Django Rest Framework  3.12.4
- psycopg2 2.9.9


2. Navigate to the project directory:
cd foodDeliveries


3. Install the required packages:
pip install -r requirements.txt


4. Apply database migrations:
python manage.py migrate


5. Collect static files:
python manage.py collectstatic


## Running the Application

Start the development server:
python manage.py runserver


Access the application in your web browser at `http://localhost:8000`.

## API Endpoints


- `/api/v1/pricing/?base_distance={total_Distane}&format=api&item_id={item_id}&organization_id={organization_id}&zone= {zone_name}  Retrives data from {zone, item_id,organization_id, base_Distance
` 

## Testing

Run the test suite with:
python manage.py test


## Contributing

Pull requests are welcome. Please ensure that all tests pass before submitting a pull request.

## License

This project is licensed under the terms of the MIT license.