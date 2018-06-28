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
                        elif cmd.startswith("openqr"): #openqr
                            number = cmd.replace("openqr","")
                            groups = client.getGroupIdsJoined()
                            try:
                                group = groups[int(number)-1]
                                G = client.getGroup(group)
                                try:
                                    G.preventedJoinByTicket = False
                                    client.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(G.id)))
                                except:
                                    G.preventedJoinByTicket = False
                                    client.updateGroup(G)
                                    gurl = "https://line.me/R/ti/g/{}".format(str(client.reissueGroupTicket(G.id)))
                                client.sendMessage(to, "「 Open Qr 」\n\nGroup : " + G.name + "\nLink: " + gurl)
                            except Exception as error:
                                client.sendMessage(to, str(error))
#------------------------------------------------------------------------------------------------------------------------------------
