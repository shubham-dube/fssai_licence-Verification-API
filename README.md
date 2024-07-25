# FSSAI Licence Verification API

This API fetches all the details of given fssai licence number with only licence number.

## Table of Contents

- [Features](#Features)
- [Installation](#Installation)
- [Usage](#Usage)
- [Endpoints](#EndPoints)
- [Support](#Support)
- [Contribution](#Contribution)

## Features
- It Needs only FSSAI Licence Number to check their Details.
- Returns the Licence Details.
- Easy to integrate in any of your application.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/shubham-dube/fssai_licence-Verification-API.git
   cd fssai_licence-Verification-API
   
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate # On Linux use `source venv/bin/activate`
   
3. Install the dependencies:
   ```bash
   pip install flask requests

4. Run the Application:
   ```bash
   python app.py
 *The API will be available at http://127.0.0.1:5000.*
 
## Usage
- Show the Licence Number input Field to the user.
- Send the entered Licence Number to the given endpoint acc. to request body.
- You will get all the details of FSSAI Licence Number in JSON Format
  
## EndPoints

### Fetching Licence Details

**Endpoint:** `/api/v1/get_fssai_details`

**Method:** `POST`

**Description:** `This Endpoint takes only the Mempership Number as Payload and return the full data of that Chatered Accountant holding that Membership Number.`

**Request Body:**
```json
{
    "licenceNumber": "21422850008902"
}
```
**Response**
```json
{
    "currentPageNo": 1,
    "pageLimit": 10,
    "paginationListRecords": [
        {
            "apptypedesc": "New Registration",
            "companyname": "AARNAV FOOD PRODUCTS/ AJAY LASHKARI",
            "displayrefid": "30221208112196945",
            "districtname": "Indore",
            "fboid": 21354201364561297,
            "licenseactiveflag": true,
            "licensecategoryid": 3,
            "licensecategoryname": "Registration",
            "licenseno": "21422850008902",
            "premiseaddress": "103-A HUKUM CHANDRA COLONY, PANCHKUIYA ROAD, INDORE, MP",
            "premisepincode": 452002,
            "refid": 112196945,
            "statename": "Madhya Pradesh",
            "statusdesc": "Registration Certificate issued",
            "talukname": "Indore",
            "villagename": "Indore"
        }
    ],
    "totalPages": 0,
    "totalRecords": 0
}
```
**Status Codes**
- 200 OK : `Details Recieved`

## Support
For Support Contact me at itzshubhamofficial@gmail.com
or Mobile Number : `+917687877772`

## Contribution

We welcome contributions to improve this project. Here are some ways you can contribute:

1. **Report Bugs:** If you find any bugs, please report them by opening an issue on GitHub.
2. **Feature Requests:** If you have ideas for new features, feel free to suggest them by opening an issue.
3. **Code Contributions:** 
    - Fork the repository.
    - Create a new branch (`git checkout -b feature-branch`).
    - Make your changes.
    - Commit your changes (`git commit -m 'Add some feature'`).
    - Push to the branch (`git push origin feature-branch`).
    - Open a pull request.

4. **Documentation:** Improve the documentation to help others understand and use the project.
5. **Testing:** Write tests to improve code coverage and ensure stability.

Please make sure your contributions adhere to our coding guidelines and standards.
