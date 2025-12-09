from mcp.server.fastmcp import FastMCP

# Création du serveur MCP pour le calculateur
calculator_mcp = FastMCP(
    name="calculator"
)

# Outil d'addition
@calculator_mcp.tool()
def add(a: float, b: float) -> str:
    
    try:
        result = float(a) + float(b)
        return f"Le résultat de {a} + {b} = {result}"
    except ValueError:
        return "Erreur: Veuillez entrer des nombres valides"

# Outil de soustraction
@calculator_mcp.tool()
def subtraction(a: float, b: float) -> str:
   
    try:
        result = float(a) - float(b)
        return f"Le résultat de {a} - {b} = {result}"
    except ValueError:
        return "Erreur: Veuillez entrer des nombres valides"

# Outil de multiplication
@calculator_mcp.tool()
def multiply(a: float, b: float) -> str:
    
    try:
        result = float(a) * float(b)
        return f"Le résultat de {a} × {b} = {result}"
    except ValueError:
        return "Erreur: Veuillez entrer des nombres valides"

# Outil de division
@calculator_mcp.tool()
def divide(a: float, b: float) -> str:
    
    try:
        a_float = float(a)
        b_float = float(b)
        
        if b_float == 0:
            return "Erreur: Division par zéro impossible"
        
        result = a_float / b_float
        return f"Le résultat de {a} ÷ {b} = {result}"
    except ValueError:
        return "Erreur: Veuillez entrer des nombres valides"
    
if __name__ == "__main__":
    calculator_mcp.run(transport="http")  