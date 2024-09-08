@client.event
async def on_presence_update(before: discord.Member, after: discord.Member):
    if after.id == my_Member_id:
        print('{} changed status to {}'.format(after.display_name,after.status))
