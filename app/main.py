from fastapi import FastAPI
from pydantic import BaseModel
from .database import get_db_connection
from fastapi.responses import HTMLResponse

app = FastAPI()


class QueryRequest(BaseModel):
    where_clause: str


@app.get("/")
def read_root():
    return {"message": "FastAPI application is running"}

@app.get("/health")
def health_check():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        return {"status": "success", "message": "Database connection is successful"}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        if conn:
            conn.close()

# returns single message including address and price enclosed in links""
@app.post("/query_properties/", response_class=HTMLResponse)
def query_properties(query_request: QueryRequest):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = f'''
            SELECT 
                Id, ListPrice, Address_City, Address_StreetNumber, Address_StreetDirSuffix, 
                Address_StreetName, Address_StreetSuffix, Address_StateOrProvince
            FROM [dbo].[Properties] 
            WHERE {query_request.where_clause}
        '''

        cursor.execute(sql)
        dataset = cursor.fetchall()

        if not dataset:
            
            return "<p>No properties found with the given criteria. Please try changing your search criteria or location.</p>"
            
        else:
            base_url = "https://aigentyportal.azurewebsites.net/details/"
            properties = []
            for row in dataset[:10]:
                street_address = " ".join(filter(None, [
                    row[3],  # Address_StreetNumber
                    row[4],  # Address_StreetDirSuffix
                    row[5],  # Address_StreetName
                    row[6]   # Address_StreetSuffix
                ]))
                address = f"{street_address}, {row[2]} {row[7]}"  # City and State
                price = f"${row[1]:,.0f}"
                link = f'<a href="{base_url}{row[0]}" target="_blank">{address} - {price}</a>'
                properties.append(f"<p>{link}</p>")
                
            formatted_message = "<p>Properties found with the given criteria:</p>" + "".join(properties)

            return formatted_message
    except Exception as e:
        return f"<p>We couldn't understand your query. Please check the syntax and try again.</p>"
    finally:
        if conn:
            conn.close()




# ------------------------------------------------------------------------
# returns litings array and message
# @app.post("/query_properties/")
# def query_properties(query_request: QueryRequest):
#     conn = None
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         sql = f'''
#             SELECT 
#                 Id, ArchitecturalStyle, StructureType, subType, BedroomCount, BathroomCount, ListPrice, Address_City, ParkingTotal, YearBuilt, LivingAreaSquareFeet
#             FROM [dbo].[Properties] 
#             WHERE {query_request.where_clause}
#         '''

#         cursor.execute(sql)
#         dataset = cursor.fetchall()
#         columns = [column[0] for column in cursor.description]
#         print(f"Columns: {columns}")

#         if not dataset:
#             return {
#                 "message": "No properties found with the given criteria",
#                 "properties": []
#             }
#         else:
#             selected_columns = ['Id', 'ArchitecturalStyle', 'StructureType', 'subType', 'BedroomCount', 'BathroomCount', 'ListPrice', 'Address_City', 'ParkingTotal', 'YearBuilt', 'LivingAreaSquareFeet']
            
#             # Create a list of dictionaries with selected columns
#             properties = []
#             for row in dataset:
#                 property_dict = {column: row[idx] for idx, column in enumerate(selected_columns)}
#                 properties.append(property_dict)
            
#             return {
#                 "message": "Properties found with the given criteria",
#                 "properties": properties
#             }
#     except Exception as e:
#         return {
#             "message": "We couldn't understand your query. Please check the syntax and try again.",
#             "error": str(e)
#         }
#     finally:
#         if conn:
#             conn.close()




# ------------------------------------------------------------------------
# returns listings links and message

# @app.post("/query_properties/")
# def query_properties(query_request: QueryRequest):
#     conn = None
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         sql = f'''
#             SELECT 
#                 Id
#             FROM [dbo].[Properties] 
#             WHERE {query_request.where_clause}
#         '''

#         cursor.execute(sql)
#         dataset = cursor.fetchall()

#         if not dataset:
#             return {
#                 "message": "No properties found with the given criteria",
#                 "properties": []
#             }
#         else:
#             base_url = "https://aigentyportal.azurewebsites.net/details/"
#             properties = [f"{base_url}{row[0]}" for row in dataset[:5]]

#             return {
#                 "message": "Properties found with the given criteria",
#                 "properties": properties
#             }
#     except Exception as e:
#         return {
#             "message": "We couldn't understand your query. Please check the syntax and try again.",
#             "error": str(e)
#         }
#     finally:
#         if conn:
#             conn.close()

# ------------------------------------------------------------------------



# # returns singles message including links ""
# @app.post("/query_properties/")
# def query_properties(query_request: QueryRequest):
#     conn = None
#     try:
#         conn = get_db_connection()
#         cursor = conn.cursor()

#         sql = f'''
#             SELECT 
#                 Id
#             FROM [dbo].[Properties] 
#             WHERE {query_request.where_clause}
#         '''

#         cursor.execute(sql)
#         dataset = cursor.fetchall()

#         if not dataset:
#             return {
#                 "message": "No properties found with the given criteria. Please try changing your search criteria or location."
#             }
#         else:
#             base_url = "https://aigentyportal.azurewebsites.net/details/"
#             properties_links = [f"{base_url}{row[0]}" for row in dataset[:5]]
#             formatted_message = "Properties found with the given criteria: " + ", ".join(properties_links)

#             return {"message": formatted_message}
#     except Exception as e:
#         return {
#             "message": f"We couldn't understand your query. Please check your message and try again."
#         }
#     finally:
#         if conn:
#             conn.close()

