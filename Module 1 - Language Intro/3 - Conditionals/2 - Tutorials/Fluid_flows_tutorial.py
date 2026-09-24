# Laminar and turbulent fluid flows in a pipe example (tutorial).

mean_fluid_velocity = 2.3           # meters per second
pipe_diameter = 0.5                 # meters
fluid_dynamic_viscosity = 0.5       # Pascal seconds
fluid_density = 1000                # kg per cubic meter

# Add the appropriate calculation for Reynolds number to the next line.
Reynolds_number = None

print("The Reynolds number is "+str(Reynolds_number))

# Change the boolean expressions to evaluate Reynolds number to determine if the flow laminar or turbulent.
if Reynolds_number == False:
    print("This flow is laminar!")

elif Reynolds_number == False:
    print("This flow is turbulent!")

elif Reynolds_number == False:
    print("This flow is transitional!")

else:
    print("Something's not right") 


# Check the results of your code against a hand calculation.    
# Try changing the initial variables - make sure that all types of flows are correctly identified.