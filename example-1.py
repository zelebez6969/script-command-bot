# daripada gada kerjaan ya buat2 aja :v
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
                        elif cmd == 'square' or cmd == ' squares': #find join square
                            a = client.getJoinedSquares()
                            squares = a.squares
                            txt2 = '「 Squares 」\n'
                            for s in range(len(squares)):
                                txt2 += "\n"+str(s+1)+". "+str(squares[s].name)
                            txt2 += "\n\nTotal {} Squares.".format(str(len(squares)))
                            txt2 += "\n\nUsage : Square#num"
                            client.sendMessage(to,str(txt2))
#------------------------------------------------------------------------------------------------------------------------------------
