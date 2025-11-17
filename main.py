# Working with sets
from pyscript import display

Varsity = {'Ishan', 'Vito', 'Tar', 'Enzo'}
Cocc = {'Tar', 'Koby', 'Vince', 'Vito'}
display("People in Varsity:", target='output')
display(Varsity, target='output')
display("People in COCC:", target='output')
display(Cocc, target='output')

# find students involved in at least one club
display("Students in at least one club:", target='output')
display(Varsity.union(Cocc), target='output')

# find students who belong to both club
display("Students in both clubs:", target='output')
display(Varsity & Cocc, target='output')

# find students in the first club
display("Students in the first club:", target='output')
display(Varsity, target='output')

# find students in the second club
display("Students in the second club:", target='output')
display(Cocc, target='output')

# find students in exactly one club
display("Students in exactly one club:", target='output')
display(Varsity ^ Cocc, target='output')
