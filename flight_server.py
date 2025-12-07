from mcp.server.fastmcp import FastMCP
import os
import json
app=FastMCP(name="FlightInfo")
FLIGHTS_PATH = os.path.join(os.path.dirname(__file__), "flights.json")

def  _load_flights():
  with open(FLIGHTS_PATH, "r", encoding="utf-8") as f:
    return json.load(f).get("flights", [])
  
@app.resource("flights://today")
def flights_resource():
  """
  Resource qui expose la liste des vols du jour.
  L'URL 'flights://today' sera visible par Copilot/Claude.
  """
  with open(FLIGHTS_PATH, "r", encoding="utf-8") as f:
    return f.read()
@app.tool()
def find_flight(flight_number: str) -> str:
   """Trouve un vol par son numéro (ex: AF1234)"""
   flights = _load_flights()
   for flight in flights:
      if flight.get("flight_number", "").upper() == flight_number.upper():
        return f"""✈️
        Vol {flight["flight_number"]} ({flight["airline"]})
        {flight["departure_city"]} → {flight["arrival_city"]}
        Départ : {flight["departure_time"]} | Arrivée :
              {flight["arrival_time"]}
        Statut : {flight["status"]}
        """
   return f"Vol {flight_number} non trouvé aujourd'hui."
@app.tool()
def flight_status(status: str) -> str:
    """Retourne la liste des vols avec le statut spécifié.
    Exemple: flight_status("Retardé")
    """
    flights = _load_flights()
    matching = [f for f in flights if f.get("status", "").upper() == status.upper()]
    
    if not matching:
        return f"Aucun vol trouvé avec le statut '{status}' aujourd'hui."
    
    response = f"Vols avec le statut '{status}' aujourd'hui :\n"
    for flight in matching:
        response += (
            f"✈️ Vol {flight['flight_number']} ({flight['airline']}) : "
            f"{flight['departure_city']} → {flight['arrival_city']} | "
            f"Départ : {flight['departure_time']} | Arrivée : {flight['arrival_time']}\n"
        )
    return response
  
if __name__ == "__main__":
    app.run(transport="stdio")
  
@app.tool()
def list_flights_by_airline(airline: str) -> str:
    """Liste tous les vols d'une compagnie aérienne donnée."""
    flights = _load_flights()
    matching_flights = [
        flight for flight in flights if flight.get("airline", "").upper() == airline.upper()
    ]
    if not matching_flights:
        return f"Aucun vol trouvé pour la compagnie aérienne {airline} aujourd'hui."
    
    response = f"Vols pour la compagnie aérienne {airline} aujourd'hui :\n"
    for flight in matching_flights:
        response += f"✈️ Vol {flight['flight_number']} : {flight['departure_city']} → {flight['arrival_city']} | Départ : {flight['departure_time']} | Arrivée : {flight['arrival_time']} | Statut : {flight['status']}\n"
    return response
