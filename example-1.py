#------------------------------------------------------------------------------------------------------------------------------------
                        elif cmd.startswith("gcastvoice "):
                                bctxt = cmd.replace("gcastvoice ", "")
                                bc = ("Broadcast voice by me")
                                cb = (bctxt + bc)
                                tts = gTTS(cb, lang='id', slow=False)
                                tts.save('tts.mp3')
                                n = client.getGroupIdsJoined()
                                for apalah in n:
                                    client.sendAudio(apalah, 'tts.mp3')
#------------------------------------------------------------------------------------------------------------------------------------
