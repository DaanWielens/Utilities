import numpy as np
import matplotlib.pyplot as plt

file = 'yourgroupchathere.txt'

chat = open(file, encoding='utf8')
chatText = chat.read()
chat.close()

i = 0
WAdb = {}
global nUsers
nUsers = 0

for line in chatText.splitlines():
    i += 1
    # The line should contain a timestamp (has length 18):
    if len(line) > 18:
        try:
            # Check if line contains timestamp:
            line = line.split(', ')[1].split(' - ')
            if line[0][2] == ':':
                # Check if line still contains a ':' (after username)
                if ':' in line[1]:
                    # Grab username
                    username = line[1].split(':')[0]

                    # When empty, add user to dictionary
                    if len(WAdb) == 0:
                        WAdb[nUsers] = [username, 1]
                        nUsers += 1


                    #If not, check if user exists. If so, raise counter. Else, create user
                    else:
                        userExist = 0
                        for val in WAdb.items():
                            if val[1][0] == username:
                                val[1][1] += 1
                                userExist = 1
                                nUsers += 1

                        if userExist == 0:
                            WAdb[nUsers] = [username, 1]
                            nUsers += 1

        except Exception:
            # The line does not contain valid information, so we don't care
            pass

# Create list
usrs = []
nmsg = []
for val in WAdb.items():
    usrs.append(val[1][0])
    nmsg.append(val[1][1])

# Sort list
usrs = np.array(usrs)
nmsg = np.array(nmsg)
idxs = nmsg.argsort()[::-1]
usrs = usrs[idxs]
nmsg = nmsg[idxs]

# Plot
fig, ax = plt.subplots()
fig.set_size_inches(10, 7)
barplt= plt.bar(range(len(usrs)), nmsg)
plt.xticks(range(len(usrs)), usrs, rotation='vertical')
plt.subplots_adjust(bottom=0.3)
plt.ylim([0, np.max(nmsg)*1.2])
plt.title('WhatsApp data of: ' + str(file).split('.')[0], weight='bold')

# Function to add labels to a barplot
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    # Get largest bar to determine offset
    ht = []
    for rect in rects:
        height = rect.get_height()
        ht.append(height)
    mht = max(ht)
    ofs = max(ht)*0.05
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., height+ofs,
                '%d' % int(height),
                ha='center', va='bottom', rotation='vertical')

# Add labels to plot
autolabel(barplt)

# Save figure
plt.tight_layout()
plt.savefig(file.split('.')[0] + '.png')
