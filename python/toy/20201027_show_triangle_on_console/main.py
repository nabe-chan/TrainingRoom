import sys



paint="＊"
space="　"
total_number_of_layer=5

# Assign arguments
if len(sys.argv) > 1:
    total_number_of_layer = int(sys.argv[1])

# main code
for i, b in enumerate(range(total_number_of_layer)):
    current_number_of_layer = i+1
    print(current_number_of_layer,
            ":",
            space*(total_number_of_layer - current_number_of_layer),
            paint*(current_number_of_layer - 1),  # exclude duplicate(center) block
            paint,  # center block (must)
            paint*(current_number_of_layer - 1),  # exclude duplicate(center) block
            space*(total_number_of_layer - current_number_of_layer),
            sep="",
            #end=";\n"
    )