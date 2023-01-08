#para mudar a cor de fundo de uma window usar o seguinte codigo---->app.configure(bg=red)
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import ImageTk,Image
from tkinter import filedialog
from tkinter import ttk
import webbrowser as wb
#Janela Pagina Inicial
def paginainicial(user):
    f=open("login.txt","r")
    for linha in f:
     login_c=str(linha)
    f.close() 
    texto2=txt_user.get()+";"+txt_password.get()+";"+txt_email.get()+";"
    pos=login_c.find(texto2)
    if pos!=-1:
     window.destroy()
     window1=Tk()
     window1.geometry("1900x950")
     window1.title("OrganizEat:Página Principal")
     bg=PhotoImage(file="mybgfinal1.gif")
     labelfundo=Label(window1,image=bg)
     labelfundo.place(x=0,y=0,relwidth=1,relheight=1)
     def publicacoes():
         window_4=Toplevel()
         window_4.title("OrganizEat:Publicações")
         window_4.geometry("1900x950")
         window_4.configure(bg="#2785bc")
         def limpar3():
             txt_ingredientes.delete("1.0","end")
             txt_titulo.delete(0,"end")
             cb_categoria.delete(0,"end")
             filename=""
             global img
             img=PhotoImage(file=filename)
             ctn_canvas.create_image(360,117,image=img)
         def publicar():
             a=open("receitas.txt","r+",encoding="utf-8")
             texto4=a.read()
             a.close()
             pos5=texto4.find(user.get()+";"+cb_categoria.get()+";"+txt_titulo.get()+";")
             if pos5!=-1:
                 messagebox.showerror("Erro","Título já existente.")
             else:
                 conteudo=user.get()+";"+cb_categoria.get()+";"+txt_titulo.get()+";"+txt_ingredientes.get("1.0","end")+";"
                 b=open("receitas.txt","a",encoding="utf-8")
                 b.write(conteudo)
                 b.close()   
                 txt_ingredientes.delete("1.0","end")
                 txt_titulo.delete(0,"end")
                 cb_categoria.delete(0,"end")
                 messagebox.showinfo("showinfo","A receita foi publicada com sucesso.")
                 e=open("receitas.txt","r",encoding="utf-8")
                 titulo_l=e.read()
                 e.close()
                 comp=len(user.get())
                 cont=titulo_l.count(user.get())
                 lista=[]
                 pos=0
                 for i in range(cont):
                     pos1=titulo_l.find(user.get(),pos)
                     pos2=titulo_l.find(";",pos1+comp+1)
                     pos3=titulo_l.find(";",pos2+1)
                     texto=titulo_l[pos2+1:pos3]
                     lista.append(texto)
                     pos=pos1+comp+1
                 lbox_receitas.delete(0,"end")
                 lbox_receitas1.delete(0,"end")
                 for receita in lista:
                     lbox_receitas.insert(END,receita)
                     lbox_receitas1.insert(END,receita)
                 global img
                 img=PhotoImage(file="fundoimagem.gif")
                 ctn_canvas.create_image(360,117,image=img)
                 window_4.update()
                 window_4.deiconify()
         def consultar():
             d=open("receitas.txt","r",encoding="utf-8")
             titulo_l1=d.read()
             d.close()
             comp1=len(lbox_receitas.get(ANCHOR))
             cont1=titulo_l1.count(lbox_receitas.get(ANCHOR))
             poss=0
             for i in range(cont1):
                 pos11=titulo_l1.find(lbox_receitas.get(ANCHOR),poss)
                 pos21=titulo_l1.find(";",pos11+comp1)
                 pos31=titulo_l1.find(";",pos21+1)
                 texto1=titulo_l1[pos21+1:pos31]
             consultar.delete("1.0","end")
             consultar.insert("end",texto1)
         def eliminar():
            f=open("receitas.txt","r",encoding="utf-8")
            texto=f.read()
            f.close()
            vezes=texto.count(user.get())
            pos1=0
            lista=[]
            for i in range(vezes):
                pos=texto.find(user.get(),pos1)
                pos2=texto.find(";",pos)
                pos3=texto.find(";",pos2+1)
                pos4=texto.find(";",pos3+1)
                pos5=texto.find(";",pos4+1)
                receitas=texto[pos:pos5]
                lista.append(receitas)
                pos1=pos5
            resultados=""
            for i in range(vezes):
                encontra=lista[i].find(lbox_receitas1.get(ANCHOR))
                if encontra!=-1:
                    resultados=lista[i]
                    texto1=texto.replace(resultados,"")
                    a=open("receitas.txt","w",encoding="utf-8")
                    a.write(texto1)
                    a.close()
                    b=open("receitas.txt","r",encoding="utf-8")
                    conteudo=b.read()
                    b.close()
                    conteudo1=conteudo.replace(";;",";")
                    c=open("receitas.txt","w",encoding="utf-8")
                    c.write(conteudo1)
                    c.close()
                    
                    break
            messagebox.showinfo("Informação","A receita foi eliminada com sucesso.")
            e=open("receitas.txt","r",encoding="utf-8")
            titulo_l=e.read()
            e.close()
            comp=len(user.get())
            cont=titulo_l.count(user.get())
            lista=[]
            pos=0
            for i in range(cont):
                pos1=titulo_l.find(user.get(),pos)
                pos2=titulo_l.find(";",pos1+comp+1)
                pos3=titulo_l.find(";",pos2+1)
                texto=titulo_l[pos2+1:pos3]
                lista.append(texto)
                pos=pos1+comp+1
            lbox_receitas.delete(0,"end")
            lbox_receitas1.delete(0,"end")
            for receita in lista:
                lbox_receitas.insert(END,receita)
                lbox_receitas1.insert(END,receita)
            window_4.update()
            window_4.deiconify()
         def consultar1():
             d=open("receitas.txt","r",encoding="utf-8")
             titulo_l1=d.read()
             d.close()
             comp1=len(lbox_receitas1.get(ANCHOR))
             cont1=titulo_l1.count(lbox_receitas1.get(ANCHOR))
             poss=0
             for i in range(cont1):
                 pos11=titulo_l1.find(lbox_receitas1.get(ANCHOR),poss)
                 pos21=titulo_l1.find(";",pos11+comp1)
                 pos31=titulo_l1.find(";",pos21+1)
                 texto1=titulo_l1[pos21+1:pos31]
             editar.delete("1.0","end")
             editar.insert("end",texto1)   
         def limpar2():
             editar.delete("1.0","end")
         def atualizarreceita():
            if lbox_receitas1.get(ANCHOR)=="" and cb_categoria1.get()=="":
                messagebox.showwarning("Informação","Não completou o processo de atualização.")
            else:
                f=open("receitas.txt","r",encoding="utf-8")
                texto=f.read()
                f.close()
                vezes=texto.count(user.get())
                pos1=0
                lista=[]
                for i in range(vezes):
                    pos=texto.find(user.get(),pos1)
                    pos2=texto.find(";",pos)
                    pos3=texto.find(";",pos2+1)
                    pos4=texto.find(";",pos3+1)
                    pos5=texto.find(";",pos4+1)
                    receitas=texto[pos:pos5]
                    lista.append(receitas)
                    pos1=pos5
                resultados=""
                for i in range(vezes):
                    encontra=lista[i].find(lbox_receitas1.get(ANCHOR))
                    if encontra!=-1:
                        resultados=lista[i]
                        texto1=texto.replace(resultados,"")
                        a=open("receitas.txt","w",encoding="utf-8")
                        a.write(texto1)
                        a.close()
                        b=open("receitas.txt","r",encoding="utf-8")
                        conteudo=b.read()
                        b.close()
                        conteudo1=conteudo.replace(";;",";")
                        c=open("receitas.txt","w",encoding="utf-8")
                        c.write(conteudo1)
                        c.close()
                        break
                conteudo=user.get()+";"+cb_categoria1.get()+";"+lbox_receitas1.get(ANCHOR)+";"+editar.get("1.0","end")+";"
                b=open("receitas.txt","a",encoding="utf-8")
                b.write(conteudo)
                b.close()   
                messagebox.showinfo("Informação","A receita foi atualizada com sucesso.")
                window_4.update()
                window_4.deiconify()
         def select():
             filename=filedialog.askopenfilename(initialdir="/",title="Select file",filetypes=(("gif files",".gif"),("all files","*.*")))
             window_4.deiconify()
             global img
             img=PhotoImage(file=filename)
             ctn_canvas.create_image(360,117,image=img)
             informacao=user.get()+";"+cb_categoria.get()+";"+txt_titulo.get()+";"+filename+";"
             f=open("imagens.txt","a",encoding="utf-8")
             f.write(informacao)
             f.close()

         #Abrir os titulos das receitas        
         frame3=LabelFrame(window_4,text="A MINHAS PUBLICAÇÕES:",width=800,heigh=750,bg="#2785bc",fg="white")
         frame3.place(x=10,y=10)
         frame5=LabelFrame(frame3,width=665,height=350,relief="sunken",bg="#2785bc",fg="white")
         frame5.place(x=10,y=10)
         lbl_consultar=Label(frame5,text="Consultar:",bg="#2785bc",fg="white")
         lbl_consultar.place(x=10,y=10)
         lbox_receitas=Listbox(frame5,height=15,width=30)
         lista=[]
         e=open("receitas.txt","r",encoding="utf-8")
         titulo_l=e.read()
         e.close()
         comp=len(user.get())
         cont=titulo_l.count(user.get())
         lista=[]
         pos=0
         lbox_receitas1=Listbox(frame3,height=15,width=30)
         for i in range(cont):
             pos1=titulo_l.find(user.get(),pos)
             pos2=titulo_l.find(";",pos1+comp+1)
             pos3=titulo_l.find(";",pos2+1)
             texto=titulo_l[pos2+1:pos3]
             lista.append(texto)
             pos=pos1+comp+1
         for receita in lista:
             lbox_receitas.insert(END,receita)
             lbox_receitas1.insert(END,receita)
         lbox_receitas.place(x=10,y=35)
         btn_consult1=Button(frame5,width=25,text="Consultar",command=consultar,fg="white",bg="#e0a000")
         btn_consult1.place(x=10,y=290)
         consultar=Text(frame5,width=53,height=18,)
         consultar.place(x=215,y=35)
         lbl_editar=Label(frame3,text="Atualizar:",bg="#2785bc",fg="white")
         lbl_editar.place(x=20,y=375)
         lbox_receitas1.place(x=20,y=398)
         editar=Text(frame3,width=53,height=18,)
         editar.place(x=225,y=398)
         a=open("categorias.txt","r")
         categoria=a.read()
         a.close()
         lenac=categoria.count(";")
         pos=0
         categoria1=[]
         for i in range(lenac):
             pos1=categoria.find(";",pos)
             pos2=categoria.find(";",pos1+1)
             categoria1.append(categoria[pos1+1:pos2])
             pos=pos2
         lenacc=len(categoria1)
         for i in range(lenacc):
             if categoria1[i]=="":
                 del categoria1[i]
         cb_categoria1=Combobox(frame3,values=categoria1)
         cb_categoria1.place(x=225,y=370)
         btn_limpar2=Button(frame3,text="Limpar",width=25,command=limpar2,fg="white",bg="#e0a000")
         btn_limpar2.place(x=267,y=695)
         btn_editar=Button(frame3,text="Atualizar",width=25,command=atualizarreceita,fg="white",bg="#e0a000")
         btn_editar.place(x=467,y=695)
         btn_consult2=Button(frame3,width=25,text="Consultar",command=consultar1,fg="white",bg="#e0a000")
         btn_consult2.place(x=20,y=655)
         btn_eliminar=Button(frame3,text="Eliminar Receita",width=25,command=eliminar,fg="white",bg="#e0a000")
         btn_eliminar.place(x=20,y=695)
         frame4=LabelFrame(window_4,text="PUBLICAR:",width=800,height=750,relief="sunken",bg="#2785bc",fg="white")
         frame4.place(x=700,y=10)
         btn_4=Button(frame4,text="LIMPAR",command=limpar3,width=30,height=3,fg="white",bg="#e0a000")
         btn_4.place(x=305,y=650)
         btn_5=Button(frame4,text="PUBLICAR",width=30,height=3,command=publicar,fg="white",bg="#e0a000")
         btn_5.place(x=550,y=650)
         lbl_categoria=Label(frame4,text="Categoria:",bg="#2785bc",fg="white")
         lbl_categoria.place(x=30,y=30)
         cb_categoria=Combobox(frame4,values=categoria1)
         cb_categoria.place(x=90,y=30)
         lbl_titulo=Label(frame4,text="Título:",bg="#2785bc",fg="white")
         lbl_titulo.place(x=30,y=75)
         txt_titulo=Entry(frame4,width="50")
         txt_titulo.place(x=70,y=75)
         lbl_ingredientes=Label(frame4,text="Receita(Ingredientes/Modo de Preparação):",bg="#2785bc",fg="white")
         lbl_ingredientes.place(x=30,y=120)
         txt_ingredientes=Text(frame4,width=90,height=15,wrap="word")
         txt_ingredientes.place(x=31,y=150)
         btn_select=Button(frame4,width=22,height=3,text="Selecionar Imagem",command=select,fg="white",bg="#e0a000")
         btn_select.place(x=33,y=650)
         ctn_canvas=Canvas(frame4,width=720,height=220,bd=2,relief="sunken")
         ctn_canvas.place(x=30,y=400)
         window_4.mainloop()
     def pesquisaavancada():
         def consultar():
             e=lista2.index(l_receitaconj.get(ANCHOR))
             treceita=lista[e]
             #autor
             e_autor.delete(0,"end")
             e_categoria.delete(0,"end")
             cos1=0
             cos=treceita.find(";",cos1)
             cos2=treceita.find(";",cos+1)
             cos3=treceita.find(";",cos2+1)
             e_autor.insert(0,treceita[cos+1:cos2])
             e_categoria.insert(0,treceita[cos2+1:cos3])
             #conteudo receita
             f=open("receitas.txt","r",encoding="utf-8")
             receita=f.read()
             f.close
             pos=receita.find(treceita)
             l=len(treceita)
             pos1=receita.find(";",pos+l)
             receitafinal=receita[pos+l:pos1]
             txt_consulta.delete("1.0","end")
             txt_consulta.insert("end",receitafinal)

             #visualizações
             a=open("visualizacoes.txt","a",encoding="utf-8")
             a.write(treceita)
             a.close()
             b=open("visualizacoes.txt","r",encoding="utf-8")
             vezess=b.read()
             b.close()
             contar=vezess.count(treceita)
             txt_v4.delete(0,"end")
             txt_v4.insert(0,contar)
             #abrir o número de likes
             l=open("likes.txt","r")
             likes=l.read()
             l.close()
             contlikes=likes.count(treceita)
             txt_like4.delete(0,"end")
             txt_like4.insert(0,contlikes)
             #comentarios
             txt_comentarios4.delete(0,"end")
             f=open("comentarios.txt","r",encoding="utf-8")
             comentario=f.read()
             f.close()
             contarc=comentario.count(treceita)
             posc0=0
             listacomentario=[]
             for i in range(contarc):
                 posc=comentario.find(treceita,posc0)
                 caracc=len(treceita)
                 posc1=comentario.find(";",posc+caracc)
                 listacomentario.append(comentario[posc+caracc:posc1-1])
                 posc0=posc1
             for i in listacomentario:
                 txt_comentarios4.insert("end",i)
             f=open("imagens.txt","r",encoding="utf-8")
             receita1=f.read()
             f.close()
             pos=receita1.find(treceita)
             l=len(treceita)
             pos1=receita1.find(";",pos+l)
             receitafinal1=receita1[pos+l:pos1]
             global img
             img=PhotoImage(file=receitafinal1)
             ctn_canas2.create_image(200,200,image=img)
         def like():
              e=lista2.index(l_receitaconj.get(ANCHOR))
              treceita=lista[e]
              l1=open("likes.txt","a")
              l1.write(treceita)
              l1.close()
              l=open("likes.txt","r")
              likes=l.read()
              l.close()
              contlikes=likes.count(treceita)
              txt_like4.delete(0,"end")
              txt_like4.insert(0,contlikes) 
              import datetime
              data=datetime.datetime.now()
              datah=data.strftime("%Y-%m-%d")
              tempo=datetime.datetime.now().time()
              tempoh=tempo.strftime("%H:%I:%S")
              dt=datah+"//"+tempoh
              cos1=0
              cos=treceita.find(";",cos1)
              cos2=treceita.find(";",cos+1)
              cos3=treceita.find(";",cos2+1)
              cos4=treceita.find(";",cos3+1)
              notifica=";"+treceita[cos+1:cos2]+";"+"Nova Notificação"+" ("+dt+")"+";"+user.get()+" adicionou um LIKE na sua receita:"+treceita[cos3+1:cos4]+"."+";"
              b=open("notificaçoes.txt","a",encoding="utf-8")
              b.write(notifica)
              b.close()
         def adicionarf():
             e=lista2.index(l_receitaconj.get(ANCHOR))
             treceita=lista[e]
             cos1=0
             cos=treceita.find(";",cos1)
             cos2=treceita.find(";",cos+1)
             cos3=treceita.find(";",cos2+1)
             cos4=treceita.find(";",cos3+1)
             textofinal=";"+user.get()+";"+treceita[cos3+1:cos4]+";"+txt_consulta.get("1.0","end")+";"
             f=open("listafavoritos.txt","a",encoding="utf-8")
             f.write(textofinal)
             f.close()
             messagebox.showinfo("Informação","A receita foi adicionada com sucesso na sua lista de favoritos")
             window_pa.update()
             window_pa.deiconify()
         def cc():
             e=lista2.index(l_receitaconj.get(ANCHOR))
             treceita=lista[e]
             comentario=treceita+user.get()+":"+txt_ccomentarios4.get("1.0","end")
             comentario2=user.get()+":"+txt_ccomentarios4.get("1.0","end")
             f=open("comentarios.txt","a",encoding="utf-8")
             f.write(comentario)
             f.close()
             import datetime
             data=datetime.datetime.now()
             datah=data.strftime("%Y-%m-%d")
             tempo=datetime.datetime.now().time()
             tempoh=tempo.strftime("%H:%I:%S")
             dt=datah+"//"+tempoh
             cos1=0
             cos=treceita.find(";",cos1)
             cos2=treceita.find(";",cos+1)
             cos3=treceita.find(";",cos2+1)
             cos4=treceita.find(";",cos3+1)
             notifica=";"+treceita[cos+1:cos2]+";"+"Nova Notificação"+" ("+dt+")"+";"+user.get()+" adicionou um comentário na sua receita:"+treceita[cos3+1:cos4]+"//"+comentario2+"."+";"
             b=open("notificaçoes.txt","a",encoding="utf-8")
             b.write(notifica)
             b.close()
             txt_comentarios4.delete("1.0","end")
         def filtrar():
             encontrar=""
             encontrar1=";"+box_filtro1.get()+";"+box_filtro2.get()+";"
             encontrar2=";"+box_filtro1.get()+";"
             encontrar3=";"+box_filtro2.get()+";"
             if cb1.get()==1:
                 encontrar=encontrar2
             if cb2.get()==1:
                 encontrar=encontrar3
             if cb3.get()==1:
                 encontrar=encontrar1
             f=open("receitas.txt","r",encoding="utf-8")
             receita=f.read()
             f.close()
             pos=0
             cont=receita.count(";")
             media=cont/4
             lista=[]
             lista2=[]
             for i in  range(int(media)+1):
                 pos1=receita.find(";",pos)
                 pos2=receita.find(";",pos1+1)
                 pos3=receita.find(";",pos2+1)
                 pos4=receita.find(";",pos3+1)
                 pos5=receita.find(";",pos4+1)
                 lista.append(receita[pos1:pos4+1])
                 texto=str(i+1)+"."+receita[pos3+1:pos4]
                 lista2.append(texto)
                 pos=pos5    
             lena=len(lista)
             for i in range(lena):
                 if lista[i]=="":
                     del lista[i]
             lena1=len(lista) 
             lena2=len(lista2)
             if lena1!=lena2:
                 del lista2[lena1]
             lista3=[]
             lista4=[]
             encontrar1=";"+box_filtro1.get()+";"+box_filtro2.get()+";"
             encontrar2=";"+box_filtro1.get()+";"
             encontrar3=";"+box_filtro2.get()+";"
             lena=len(lista)
             for i in range(lena):
                  pos=str(lista[i]).find(encontrar)
                  if pos==0:
                      lista3.append(lista[i])
                      lista4.append(lista2[i])
             lista2=lista4
             if lista2==[]:
                 messagebox.showwarning("Informação","Não foi possível filtrar.")
                 window_pa.update()
                 window_pa.deiconify()
             else:    
                 l_receitaconj.delete(0,"end")
                 for item in lista2:
                     l_receitaconj.insert("end",item)
         def pesquisar():
             f=open("receitas.txt","r",encoding="utf-8")
             consultar=f.read()
             f.close()
             cont=consultar.count(";")
             mediap=cont/4
             pos=0
             listap=[]
             for i in range(int(mediap)+1):
                 pos1=consultar.find(";",pos)
                 pos2=consultar.find(";",pos1+1)
                 pos3=consultar.find(";",pos2+1)
                 pos4=consultar.find(";",pos3+1)
                 pos5=consultar.find(";",pos4+1)
                 pos6=consultar[pos4:pos5].count(entry_filtro.get())
                 if pos6!=0:
                     listap.append(consultar[pos:pos4+1])
                 pos=pos5
             f=open("receitas.txt","r",encoding="utf-8")
             receita=f.read()
             f.close()
             pos=0
             cont=receita.count(";")
             media=cont/4
             lista=[]
             lista2=[]
             for i in  range(int(media)+1):
                 pos1=receita.find(";",pos)
                 pos2=receita.find(";",pos1+1)
                 pos3=receita.find(";",pos2+1)
                 pos4=receita.find(";",pos3+1)
                 pos5=receita.find(";",pos4+1)
                 lista.append(receita[pos1:pos4+1])
                 texto=str(i+1)+"."+receita[pos3+1:pos4]
                 lista2.append(texto)
                 pos=pos5    
             lena=len(lista)
             for i in range(lena):
                 if lista[i]=="":
                     del lista[i]
             lena1=len(lista) 
             lena2=len(lista2)
             if lena1!=lena2:
                 del lista2[lena1]
             lista3=[]
             lena3=len(listap)
             for i in range(lena3):
                 posl=lista.index(listap[i])
                 lista3.append(lista2[posl])
             lista2=lista3
             if lista2==[]:
                 messagebox.showwarning("Informação","Não foi possível filtrar.")
                 window_pa.update()
                 window_pa.deiconify()
             else:    
                 l_receitaconj.delete(0,"end")
                 for item in lista2:
                     l_receitaconj.insert("end",item) 
         def ordernarv():
              f=open("receitas.txt","r",encoding="utf-8")
              receitas=f.read()
              f.close()
              pos=0
              listav=[]
              listanv=[]
              cont=receitas.count(";")
              media=cont/4
              for i in range(int(media)):
                  pos1=receitas.find(";",pos)
                  pos2=receitas.find(";",pos1+1)
                  pos3=receitas.find(";",pos2+1)
                  pos4=receitas.find(";",pos3+1)
                  pos5=receitas.find(";",pos4+1)
                  listav.append(receitas[pos1:pos4+1])
                  listanv.append(receitas[pos3+1:pos4])
                  pos=pos5
              a=open("visualizacoes.txt","r",encoding="utf-8")
              le=a.read()
              a.close()
              lista1v=[]
              lis=len(listav)
              for i in range(lis):
                 cont=le.count(listav[i])
                 lista1v.append(cont)
              lista2v=lista1v.copy()
              lista2v.sort()
              lista2v.reverse()
              cont2=len(lista2v)
              lista4v=[]
              for i in range(cont2):
                 ss=lista1v.index(lista2v[i])
                 lista4v.append(str(listav[ss]))  
              lena3=len(lista4v)
              lista5=[]
              for i in range(lena3):
                  posv=lista.index(lista4v[i])
                  lista5.append(lista2[posv])
              l_receitaconj.delete(0,"end")
              for item in lista5:
                  l_receitaconj.insert("end",item)
         def ordernarl():
             f=open("receitas.txt","r",encoding="utf-8")
             receitas=f.read()
             f.close()
             pos=0
             listal=[]
             listanl=[]
             cont=receitas.count(";")
             media=cont/4
             for i in range(int(media)):
                 pos1=receitas.find(";",pos)
                 pos2=receitas.find(";",pos1+1)
                 pos3=receitas.find(";",pos2+1)
                 pos4=receitas.find(";",pos3+1)
                 pos5=receitas.find(";",pos4+1)
                 listal.append(receitas[pos1:pos4+1])
                 listanl.append(receitas[pos3+1:pos4])
                 pos=pos5
             a1=open("likes.txt","r")
             le=a1.read()
             a1.close()
             lista11=[] 
             lis1=len(listal)
             for i in range(lis1):
                 cont=le.count(listal[i])
                 lista11.append(cont)
             lista21=lista11.copy()
             lista21.sort()
             lista21.reverse()
             cont21=len(lista21)
             lista41=[] 
             for i in range(cont21):
                 ss=lista11.index(lista21[i])
                 lista41.append(str(listal[ss]))
                 lena3=len(lista41)
             lista5=[]
             for i in range(lena3):
                 posv=lista.index(lista41[i])
                 lista5.append(lista2[posv])
             l_receitaconj.delete(0,"end")
             for item in lista5:
                 l_receitaconj.insert("end",item)
         def repor():
              f=open("receitas.txt","r",encoding="utf-8")
              receita=f.read()
              f.close()
              pos=0
              cont=receita.count(";")
              media=cont/4
              lista=[]
              lista2=[]
              for i in  range(int(media)+1):
                 pos1=receita.find(";",pos)
                 pos2=receita.find(";",pos1+1)
                 pos3=receita.find(";",pos2+1)
                 pos4=receita.find(";",pos3+1)
                 pos5=receita.find(";",pos4+1)
                 lista.append(receita[pos1:pos4+1])
                 texto=str(i+1)+"."+receita[pos3+1:pos4]
                 lista2.append(texto)
                 pos=pos5    
              lena=len(lista)
              for i in range(lena):
                 if lista[i]=="":
                     del lista[i]
              lena1=len(lista) 
              lena2=len(lista2)
              if lena1!=lena2:
                 del lista2[lena1]
              l_receitaconj.delete(0,"end")
              for item in lista2:
                 l_receitaconj.insert("end",item)
         #Começa aqui...
         window_pa=Toplevel() 
         window_pa.geometry("1500x780")
         window_pa.title("OrganizEat:Catálogo de Receitas:Pesquisa Avançada")
         window_pa.configure(bg="#2785bc")
         lbl_conjunto=LabelFrame(window_pa,text="Catálogo de Receitas",width=1480,height=750,bg="#2785bc",fg="white")
         lbl_conjunto.place(x=10,y=10)
         l_receitaconj=Listbox(lbl_conjunto,width=37,height=21,)
         l_receitaconj.place(x=10,y=10)
         l_categoria=Label(lbl_conjunto,text="Categoria:",bg="#2785bc",fg="white")
         l_categoria.place(x=1063,y=10)
         e_categoria=Entry(lbl_conjunto,width=35)
         e_categoria.place(x=1127,y=10)
         l_autor=Label(lbl_conjunto,text="Autor:",bg="#2785bc",fg="white")
         l_autor.place(x=1063,y=40)
         e_autor=Entry(lbl_conjunto,width=35)
         e_autor.place(x=1127,y=40)
         btn_consult4=Button(lbl_conjunto,text="Consultar",width=31,height=3,command=consultar,fg="white",bg="#e0a000")
         btn_consult4.place(x=10,y=360)
         btn_adicionar=Button(lbl_conjunto,text="Adicionar à minha Lista de Favoritas",width=31,height=3,command=adicionarf,fg="white",bg="#e0a000")
         btn_adicionar.place(x=10,y=420)
         txt_consulta=Text(lbl_conjunto,width=100,height=30)
         txt_consulta.place(x=250,y=10)
         ctn_canas2=Canvas(lbl_conjunto,width=400,height=400,bd=2,relief="sunken")
         ctn_canas2.place(y=87,x=1063)
         lbl_outro4=LabelFrame(lbl_conjunto,width=940,height=220,bg="#2785bc",fg="white",relief="sunken")
         lbl_outro4.place(x=520,y=508)
         lbl_comentarios4=Label(lbl_outro4,text="Comentários:",bg="#2785bc",fg="white")
         lbl_comentarios4.place(x=180,y=10)
         txt_comentarios4=Listbox(lbl_outro4,width=40,height=11)
         txt_comentarios4.place(x=180,y=30)
         lbl_ccomentarios4=Label(lbl_outro4,text="Criar Comentário:",bg="#2785bc",fg="white")
         lbl_ccomentarios4.place(x=470,y=10)
         txt_ccomentarios4=Text(lbl_outro4,width=45,height=8)
         txt_ccomentarios4.place(x=470,y=30)
         btn_ccomentário4=Button(lbl_outro4,text="Criar Comentário",width=51,command=cc,fg="white",bg="#e0a000")
         btn_ccomentário4.place(x=470,y=170)
         lbl_like4=Label(lbl_outro4,text="Nº. de Likes:",bg="#2785bc",fg="white")
         lbl_like4.place(x=10,y=60)
         txt_like4=Entry(lbl_outro4,width=18)
         txt_like4.place(x=10,y=80)
         btn_like4=Button(lbl_outro4,text="Like",width=15,height=6,command=like,fg="white",bg="#e0a000")
         btn_like4.place(x=10,y=110)
         lbl_v4=Label(lbl_outro4,text="Nº. de Visualizações:",bg="#2785bc",fg="white")
         lbl_v4.place(x=10,y=10)
         txt_v4=Entry(lbl_outro4,width=18,)
         txt_v4.place(x=10,y=30)
         lbl_frame_filtros=LabelFrame(lbl_conjunto,text="Filtros",width=490,height=227,bg="#2785bc",fg="white",relief="sunken")
         lbl_frame_filtros.place(x=10,y=500)
         filtros=Label(lbl_frame_filtros,text="Pesquisar Ingrediente:",bg="#2785bc",fg="white")
         filtros.place(x=10,y=10)
         entry_filtro=Entry(lbl_frame_filtros,width=55)
         entry_filtro.place(x=135,y=10)
         btn_pesquisar=Button(lbl_frame_filtros,text="PESQUISAR",width=46,command=pesquisar,fg="white",bg="#e0a000")
         btn_pesquisar.place(x=135,y=40)
         cb1=IntVar()
         cb2=IntVar()
         cb3=IntVar()
         cb1_escolha=Checkbutton(lbl_frame_filtros,text="Autor:",variable=cb1,command=filtrar,bg="#2785bc",fg="yellow")
         cb2_escolha=Checkbutton(lbl_frame_filtros,text="Categoria:",variable=cb2,command=filtrar,bg="#2785bc",fg="yellow")
         cb3_escolha=Checkbutton(lbl_frame_filtros,text="Todos os Filtros(Autor e Categoria)",variable=cb3,command=filtrar,bg="#2785bc",fg="yellow")
         cb1_escolha.place(x=10,y=80)
         cb2_escolha.place(x=10,y=120)
         cb3_escolha.place(x=10,y=160)
         l=open("login.txt","r")
         autor=l.read()
         l.close()
         lenaa=autor.count(";")
         mediaa=lenaa/3
         pos=0
         lista_autor=[]
         for i in range(int(mediaa)+1):
             pos1=autor.find(";",pos)
             pos2=autor.find(";",pos1+1)
             pos3=autor.find(";",pos2+1)
             pos4=autor.find(";",pos3+1)
             lista_autor.append(autor[pos1+1:pos2])
             pos=pos4
         lenaa1=len(lista_autor)
         for i in range(lenaa1):
             if lista_autor[i]=="":
                 del lista_autor[i]
         box_filtro1=Combobox(lbl_frame_filtros,width=20,values=lista_autor)
         box_filtro1.place(x=90,y=80)
         a=open("categorias.txt","r")
         categoria=a.read()
         a.close()
         lenac=categoria.count(";")
         pos=0
         listacategoria=[]
         for i in range(lenac):
             pos1=categoria.find(";",pos)
             pos2=categoria.find(";",pos1+1)
             listacategoria.append(categoria[pos1+1:pos2])
             pos=pos2
         lenacc=len(listacategoria)
         for i in range(lenacc):
             if listacategoria[i]=="":
                 del listacategoria[i]
         box_filtro2=Combobox(lbl_frame_filtros,width=20,values=listacategoria)
         box_filtro2.place(x=90,y=120)
         btn_ov=Button(lbl_frame_filtros,text="Ordernar por Visualizações",width=20,command=ordernarv,fg="white",bg="#e0a000")
         btn_ov.place(x=290,y=80)
         btn_ol=Button(lbl_frame_filtros,text="Ordernar por Likes",width=20,command=ordernarl,fg="white",bg="#e0a000")
         btn_ol.place(x=290,y=120)
         btn_repor=Button(lbl_frame_filtros,text="Repor Catálogo",width=20,command=repor,fg="white",bg="#e0a000")
         btn_repor.place(x=290,y=160)
         f=open("receitas.txt","r",encoding="utf-8")
         receita=f.read()
         f.close()
         pos=0
         cont=receita.count(";")
         media=cont/4
         lista=[]
         lista2=[]
         for i in  range(int(media)+1):
              pos1=receita.find(";",pos)
              pos2=receita.find(";",pos1+1)
              pos3=receita.find(";",pos2+1)
              pos4=receita.find(";",pos3+1)
              pos5=receita.find(";",pos4+1)
              lista.append(receita[pos1:pos4+1])
              texto=str(i+1)+"."+receita[pos3+1:pos4]
              lista2.append(texto)
              pos=pos5    
         lena=len(lista)
         for i in range(lena):
             if lista[i]=="":
                 del lista[i]
         lena1=len(lista) 
         lena2=len(lista2)
         if lena1!=lena2:
             del lista2[lena1]
         for item in lista2:
             l_receitaconj.insert("end",item)
         window_pa.mainloop()
     def notificacoes():
         window_n=Toplevel()
         window_n.geometry("525x250")
         window_n.title("OrganizEat:Notificações")
         window_n.configure(bg="#2785bc")
         def vern():
             l_t.delete("1.0","end")
             f=open("notificaçoes.txt","r+",encoding="utf-8")
             notifica=f.read()
             f.close()
             procura=";"+user.get()+";"+l_n.get(ANCHOR)+";"
             numero=len(procura)
             posn=notifica.find(procura)
             posn1=notifica.find(";",posn+numero)
             l_t.insert("end",notifica[posn+numero:posn1])
             l_n.delete(ANCHOR)
             notifica1=notifica.replace(notifica[posn:posn1+1],"")
             c=open("notificaçoes.txt","w",encoding="utf-8")
             c.write(notifica1)
             c.close()
         t_n=Label(window_n,text="Notificações:",bg="#2785bc",fg="white")
         t_n.place(x=10,y=10)
         l_n=Listbox(window_n,width=35,height=10,relief="sunken")
         l_n.place(x=10,y=40)
         l_t=Text(window_n,width=34,height=12)
         l_t.place(x=240,y=40)
         btn_n=Button(window_n,width=29,text="VER NOTIFICAÇÃO",command=vern,bg="#e0a000",fg="white")
         btn_n.place(x=10,y=211)
         f=open("notificaçoes.txt","r",encoding="utf-8")
         notifica=f.read()
         f.close()
         utilizador=";"+user.get()+";"
         cont=notifica.count(utilizador)
         pos0=0
         lista=[]
         for i in range(cont):
             lena=len(utilizador)
             pos=notifica.find(utilizador,pos0)
             pos1=notifica.find(";",pos+lena)
             lista.append(notifica[pos+lena:pos1])
             pos0=pos1
         for notificao in lista:
             l_n.insert(END,notificao)
         window.mainloop()
     def rf():
         window_rf=Toplevel()
         window_rf.geometry("800x500")
         window_rf.title("OrganizEat:As Minhas Receitas Favoritas")
         window_rf.configure(bg="#2785bc")
         def consultarf():
             lt.delete("1.0","end")
             f=open("listafavoritos.txt","r+",encoding="utf-8")
             receita=f.read()
             f.close()
             procura=";"+user.get()+";"+lb.get(ANCHOR)+";"
             numero=len(procura)
             posn=receita.find(procura)
             posn1=receita.find(";",posn+numero)
             lt.insert("end",receita[posn+numero:posn1])
         l_name=Label(window_rf,text="As Minhas Favoritas:",fg="white",bg="#2785bc")
         l_name.place(x=10,y=10)
         lb=Listbox(window_rf,width=30,height=25,relief="sunken")
         lb.place(x=10,y=30)
         lt=Text(window_rf,width=72,height=28)
         lt.place(x=210,y=30)
         btn_f=Button(window_rf,width=25,text="CONSULTAR",height=2,command=consultarf,fg="white",bg="#e0a000")
         btn_f.place(x=10,y=440)
         f=open("listafavoritos.txt","r",encoding="utf-8")
         favorita=f.read()
         f.close()
         utlizador=";"+user.get()+";"
         cont=favorita.count(utlizador)
         lista=[]
         pos=0
         contar=len(utlizador)
         for i in range(cont):
             pos1=favorita.find(utlizador,pos)
             pos2=favorita.find(";",pos1+contar)
             lista.append(favorita[pos1+contar:pos2])
             pos=pos2
         for item in lista:
             lb.insert("end",item)
         window_rf.mainloop()
     def tomr():
         window_tomr=Toplevel()
         window_tomr.geometry("710x320")
         window_tomr.title("OrganizEat:Top of Most Rated")
         window_tomr.configure(bg="#2785bc")
         l_tof=Label(window_tomr,text="Top of Most Rated",bg="#2785bc",fg="white")
         l_tof.place(x=10,y=10)
         lbl1=LabelFrame(window_tomr,text="Por visualizações:",width=320,height=263,relief="sunken",bg="#2785bc",fg="white")
         lbl1.place(x=10,y=40)
         tree=ttk.Treeview(lbl1,columns=("Receita","Visualizações"),show="headings")
         tree.column("Receita",anchor="c",width=200)
         tree.column("Visualizações",anchor="c",width=100)
         tree.heading("Receita",text="Receita:")
         tree.heading("Visualizações",text="Visualizações:")
         tree.place(x=5,y=5)
         lbl2=LabelFrame(window_tomr,text="Por Likes:",width=320,height=263,relief="sunken",bg="#2785bc",fg="white")
         lbl2.place(x=380,y=40)
         tree2=ttk.Treeview(lbl2,columns=("Receita","Likes"),show="headings")
         tree2.column("Receita",anchor="c",width=200)
         tree2.column("Likes",anchor="c",width=100)
         tree2.heading("Receita",text="Receita:")
         tree2.heading("Likes",text="Likes:")
         tree2.place(x=5,y=5)
         f=open("receitas.txt","r",encoding="utf-8")
         receitas=f.read()
         f.close()
         pos=0
         lista=[]
         listan=[]
         cont=receitas.count(";")
         media=cont/4
         for i in range(int(media)):
             pos1=receitas.find(";",pos)
             pos2=receitas.find(";",pos1+1)
             pos3=receitas.find(";",pos2+1)
             pos4=receitas.find(";",pos3+1)
             pos5=receitas.find(";",pos4+1)
             lista.append(receitas[pos1:pos4+1])
             listan.append(receitas[pos3+1:pos4])
             pos=pos5
         f=open("receitas.txt","r",encoding="utf-8")
         receitas=f.read()
         f.close()
         pos=0
         lista=[]
         listan=[]
         cont=receitas.count(";")
         media=cont/4
         for i in range(int(media)):
             pos1=receitas.find(";",pos)
             pos2=receitas.find(";",pos1+1)
             pos3=receitas.find(";",pos2+1)
             pos4=receitas.find(";",pos3+1)
             pos5=receitas.find(";",pos4+1)
             lista.append(receitas[pos1:pos4+1])
             listan.append(receitas[pos3+1:pos4])
             pos=pos5
         a=open("visualizacoes.txt","r",encoding="utf-8")
         le=a.read()
         a.close()
         lista1=[]
         lis=len(lista)
         for i in range(lis):
             cont=le.count(lista[i])
             lista1.append(cont)
             lista2=lista1.copy()
             lista2.sort()
             lista2.reverse()
         cont2=len(lista2)
         lista4=[]
         for i in range(cont2):
             ss=lista1.index(lista2[i])
             lista4.append(str(listan[ss]))
             lista4.append(str(lista2[i]))
         lena1=len(lista4)/2
         poss=0
         poss1=1
         for i in range(int(lena1)):
             tree.insert("","end",values=(lista4[poss],lista4[poss1]))
             poss=poss+2
             poss1=poss1+2
         a1=open("likes.txt","r")
         le=a1.read()
         a1.close()
         lista11=[] 
         lis1=len(lista)
         for i in range(lis1):
             cont=le.count(lista[i])
             lista11.append(cont)
         lista21=lista11.copy()
         lista21.sort()
         lista21.reverse()
         cont21=len(lista21)
         lista41=[]
         for i in range(cont21):
             ss=lista11.index(lista21[i])
             lista41.append(str(listan[ss]))
             lista41.append(str(lista21[i]))
         lena2=len(lista41)/2
         posss=0
         posss1=1    
         for i in range(int(lena2)):
             tree2.insert("","end",values=(lista41[posss],lista41[posss1]))
             posss=posss+2
             posss1=posss1+2
         window_tomr.mainloop()
     def manager():
         if user.get()!="admin":
             messagebox.showerror("Informação","Acesso Restrito.")
         else:
             window_m=Toplevel()
             window_m.geometry("730x500")
             window_m.title("OrganizEat:Gestão")
             window_m.configure(bg="#2785bc")
             def addcategoria():
                 texto=ecate.get()+";"
                 f=open("categorias.txt","a",encoding="utf-8")
                 f.write(texto)
                 f.close()
                 a=open("categorias.txt","r")
                 categoria=a.read()
                 a.close()
                 lenac=categoria.count(";")
                 pos=0
                 listacategoria=[]
                 for i in range(lenac):
                     pos1=categoria.find(";",pos)
                     pos2=categoria.find(";",pos1+1)
                     listacategoria.append(categoria[pos1+1:pos2])
                     pos=pos2
                 lenacc=len(listacategoria)
                 for i in range(lenacc):
                     if listacategoria[i]=="":
                         del listacategoria[i]
                 ecate.delete(0,"end")
                 boxcat.delete(0,"end")
                 for item in listacategoria:
                     boxcat.insert("end",item)
             def removecat():
                 texto=boxcat.get(ANCHOR)
                 boxcat.delete(ANCHOR)
                 f=open("categorias.txt","r",encoding="utf-8")
                 receita=f.read()
                 f.close()
                 receita1=receita.replace(texto,"")
                 receita2=receita1.replace(";;",";")
                 a=open("categorias.txt","w",encoding="utf-8")
                 a.write(receita2)
                 a.close()
             lcategoria=LabelFrame(window_m,text="Categorias:",width=320,height=480,fg="white",bg="#2785bc",relief="sunken")
             lcategoria.place(x=10,y=10)
             a=open("categorias.txt","r")
             categoria=a.read()
             a.close()
             lenac=categoria.count(";")
             pos=0
             listacategoria=[]
             for i in range(lenac):
                 pos1=categoria.find(";",pos)
                 pos2=categoria.find(";",pos1+1)
                 listacategoria.append(categoria[pos1+1:pos2])
                 pos=pos2
             lenacc=len(listacategoria)
             for i in range(lenacc):
                 if listacategoria[i]=="":
                     del listacategoria[i]
             boxcat=Listbox(lcategoria,width=50,height=20,)
             boxcat.place(x=5,y=5)
             for item in listacategoria:
                 boxcat.insert("end",item)
             def dellreceita():
                 e=lista2.index(boxrec.get(ANCHOR))
                 boxrec.delete(ANCHOR)
                 treceita=lista[e]
                 f=open("receitas.txt","r",encoding="utf-8")
                 receita=f.read()
                 f.close
                 pos=receita.find(treceita)
                 l=len(treceita)
                 pos1=receita.find(";",pos+l)
                 receitafinal=receita[pos+l:pos1]
                 final=treceita+receitafinal
                 receita1=receita.replace(str(final),"")
                 a=open("receitas.txt","w",encoding="utf-8")
                 a.write(receita1)
                 a.close()    
             btn_de=Button(lcategoria,text="REMOVER CATEGORIA",width=42,command=removecat,fg="white",bg="#e0a000")
             btn_de.place(x=5,y=340)
             ecate=Entry(lcategoria,width=49)
             ecate.place(x=5,y=380)
             btn_de=Button(lcategoria,text="ADICIONAR CATEGORIA",width=42,command=addcategoria,fg="white",bg="#e0a000")
             btn_de.place(x=5,y=420)
             lreceita=LabelFrame(window_m,text="Receitas:",width=320,height=480,fg="white",bg="#2785bc",relief="sunken")
             lreceita.place(x=400,y=10)
             boxrec=Listbox(lreceita,width=50,height=20)
             boxrec.place(x=5,y=5)
             btn_de=Button(lreceita,text="REMOVER RECEITA",width=42,height=4,command=dellreceita,fg="white",bg="#e0a000")
             btn_de.place(x=5,y=340)
             f=open("receitas.txt","r",encoding="utf-8")
             receita=f.read()
             f.close()
             pos=0
             cont=receita.count(";")
             media=cont/4
             lista=[]
             lista2=[]
             for i in  range(int(media)+1):
                pos1=receita.find(";",pos)
                pos2=receita.find(";",pos1+1)
                pos3=receita.find(";",pos2+1)
                pos4=receita.find(";",pos3+1)
                pos5=receita.find(";",pos4+1)
                lista.append(receita[pos1:pos4+1])
                texto=str(i+1)+"."+receita[pos3+1:pos4]
                lista2.append(texto)
                pos=pos5    
             lena=len(lista)
             for i in range(lena):
                 if lista[i]=="":
                     del lista[i]
             lena1=len(lista) 
             lena2=len(lista2)
             if lena1!=lena2:
                 del lista2[lena1]
             for item in lista2:
                 boxrec.insert("end",item)
             window_m.mainloop()
     def sair():
         window1.destroy()
     barra_Menu=Menu(window1)
     #Opções de inicio
     simuladores_Menu=Menu(barra_Menu)
     simuladores_Menu.add_command(label="Ajuda")
     simuladores_Menu.add_command(label="Sair",command=sair)
     barra_Menu.add_cascade(label="Inicio",menu=simuladores_Menu)
     barra_Menu.add_command(label="Publicações",command=publicacoes)
     cr_Menu=Menu(barra_Menu)
     cr_Menu.add_command(label="Top of Most Rated",command=tomr)
     cr_Menu.add_command(label="Pesquisa Avançada",command=pesquisaavancada)
     cr_Menu.add_command(label="Receitas Favoritas",command=rf)
     barra_Menu.add_cascade(label="Catálogo de Receitas",menu=cr_Menu)
     barra_Menu.add_command(label="Notificações",command=notificacoes)
     barra_Menu.add_command(label="Gestão",command=manager)
     window1.configure(menu=barra_Menu)
     
     #Conteudo Página Principal
     lbl_welcome=Label(window1,text="Bem-Vindo,",bg="#dbd4c1",font=("Arial",40))
     lbl_welcome.place(x=530,y=520)
     lbl_wn=Label(window1,text=user.get(),fg="grey",bg="#dbd4c1",font=("Arial",30))
     lbl_wn.place(x=820,y=523)
     window1.mainloop()
    else:
     messagebox.showerror("Erro","Credenciais Inválidas.")
def modoanonimo(user):
     window.destroy()
     window1=Tk()
     window1.geometry("1900x950")
     window1.title("OrganizEat:Página Principal")
     window1.title("OrganizEat:Página Principal")
     bg=PhotoImage(file="mybgfinal1.gif")
     labelfundo=Label(window1,image=bg)
     labelfundo.place(x=0,y=0,relwidth=1,relheight=1)
     def pesquisaavancada():
         def consultar():
             e=lista2.index(l_receitaconj.get(ANCHOR))
             treceita=lista[e]
             #autor
             e_autor.delete(0,"end")
             e_categoria.delete(0,"end")
             cos1=0
             cos=treceita.find(";",cos1)
             cos2=treceita.find(";",cos+1)
             cos3=treceita.find(";",cos2+1)
             e_autor.insert(0,treceita[cos+1:cos2])
             e_categoria.insert(0,treceita[cos2+1:cos3])
             #conteudo receita
             f=open("receitas.txt","r",encoding="utf-8")
             receita=f.read()
             f.close
             pos=receita.find(treceita)
             l=len(treceita)
             pos1=receita.find(";",pos+l)
             receitafinal=receita[pos+l:pos1]
             txt_consulta.delete("1.0","end")
             txt_consulta.insert("end",receitafinal)

             #visualizações
             a=open("visualizacoes.txt","a",encoding="utf-8")
             a.write(treceita)
             a.close()
             b=open("visualizacoes.txt","r",encoding="utf-8")
             vezess=b.read()
             b.close()
             contar=vezess.count(treceita)
             txt_v4.delete(0,"end")
             txt_v4.insert(0,contar)
             #abrir o número de likes
             l=open("likes.txt","r")
             likes=l.read()
             l.close()
             contlikes=likes.count(treceita)
             txt_like4.delete(0,"end")
             txt_like4.insert(0,contlikes)
             #comentarios
             txt_comentarios4.delete(0,"end")
             f=open("comentarios.txt","r",encoding="utf-8")
             comentario=f.read()
             f.close()
             contarc=comentario.count(treceita)
             posc0=0
             listacomentario=[]
             for i in range(contarc):
                 posc=comentario.find(treceita,posc0)
                 caracc=len(treceita)
                 posc1=comentario.find(";",posc+caracc)
                 listacomentario.append(comentario[posc+caracc:posc1-1])
                 posc0=posc1
             for i in listacomentario:
                 txt_comentarios4.insert("end",i)
             f=open("imagens.txt","r",encoding="utf-8")
             receita1=f.read()
             f.close()
             pos=receita1.find(treceita)
             l=len(treceita)
             pos1=receita1.find(";",pos+l)
             receitafinal1=receita1[pos+l:pos1]
             global img
             img=PhotoImage(file=receitafinal1)
             ctn_canas2.create_image(200,200,image=img)
         def filtrar():
             encontrar=""
             encontrar1=";"+box_filtro1.get()+";"+box_filtro2.get()+";"
             encontrar2=";"+box_filtro1.get()+";"
             encontrar3=";"+box_filtro2.get()+";"
             if cb1.get()==1:
                 encontrar=encontrar2
             if cb2.get()==1:
                 encontrar=encontrar3
             if cb3.get()==1:
                 encontrar=encontrar1
             f=open("receitas.txt","r",encoding="utf-8")
             receita=f.read()
             f.close()
             pos=0
             cont=receita.count(";")
             media=cont/4
             lista=[]
             lista2=[]
             for i in  range(int(media)+1):
                 pos1=receita.find(";",pos)
                 pos2=receita.find(";",pos1+1)
                 pos3=receita.find(";",pos2+1)
                 pos4=receita.find(";",pos3+1)
                 pos5=receita.find(";",pos4+1)
                 lista.append(receita[pos1:pos4+1])
                 texto=str(i+1)+"."+receita[pos3+1:pos4]
                 lista2.append(texto)
                 pos=pos5    
             lena=len(lista)
             for i in range(lena):
                 if lista[i]=="":
                     del lista[i]
             lena1=len(lista) 
             lena2=len(lista2)
             if lena1!=lena2:
                 del lista2[lena1]
             lista3=[]
             lista4=[]
             encontrar1=";"+box_filtro1.get()+";"+box_filtro2.get()+";"
             encontrar2=";"+box_filtro1.get()+";"
             encontrar3=";"+box_filtro2.get()+";"
             lena=len(lista)
             for i in range(lena):
                  pos=str(lista[i]).find(encontrar)
                  if pos==0:
                      lista3.append(lista[i])
                      lista4.append(lista2[i])
             lista2=lista4
             if lista2==[]:
                 messagebox.showwarning("Informação","Não foi possível filtrar.")
                 window_pa.update()
                 window_pa.deiconify()
             else:    
                 l_receitaconj.delete(0,"end")
                 for item in lista2:
                     l_receitaconj.insert("end",item)
         def pesquisar():
             f=open("receitas.txt","r",encoding="utf-8")
             consultar=f.read()
             f.close()
             cont=consultar.count(";")
             mediap=cont/4
             pos=0
             listap=[]
             for i in range(int(mediap)+1):
                 pos1=consultar.find(";",pos)
                 pos2=consultar.find(";",pos1+1)
                 pos3=consultar.find(";",pos2+1)
                 pos4=consultar.find(";",pos3+1)
                 pos5=consultar.find(";",pos4+1)
                 pos6=consultar[pos4:pos5].count(entry_filtro.get())
                 if pos6!=0:
                     listap.append(consultar[pos:pos4+1])
                 pos=pos5
             f=open("receitas.txt","r",encoding="utf-8")
             receita=f.read()
             f.close()
             pos=0
             cont=receita.count(";")
             media=cont/4
             lista=[]
             lista2=[]
             for i in  range(int(media)+1):
                 pos1=receita.find(";",pos)
                 pos2=receita.find(";",pos1+1)
                 pos3=receita.find(";",pos2+1)
                 pos4=receita.find(";",pos3+1)
                 pos5=receita.find(";",pos4+1)
                 lista.append(receita[pos1:pos4+1])
                 texto=str(i+1)+"."+receita[pos3+1:pos4]
                 lista2.append(texto)
                 pos=pos5    
             lena=len(lista)
             for i in range(lena):
                 if lista[i]=="":
                     del lista[i]
             lena1=len(lista) 
             lena2=len(lista2)
             if lena1!=lena2:
                 del lista2[lena1]
             lista3=[]
             lena3=len(listap)
             for i in range(lena3):
                 posl=lista.index(listap[i])
                 lista3.append(lista2[posl])
             lista2=lista3
             if lista2==[]:
                 messagebox.showwarning("Informação","Não foi possível filtrar.")
                 window_pa.update()
                 window_pa.deiconify()
             else:    
                 l_receitaconj.delete(0,"end")
                 for item in lista2:
                     l_receitaconj.insert("end",item) 
         def ordernarv():
              f=open("receitas.txt","r",encoding="utf-8")
              receitas=f.read()
              f.close()
              pos=0
              listav=[]
              listanv=[]
              cont=receitas.count(";")
              media=cont/4
              for i in range(int(media)):
                  pos1=receitas.find(";",pos)
                  pos2=receitas.find(";",pos1+1)
                  pos3=receitas.find(";",pos2+1)
                  pos4=receitas.find(";",pos3+1)
                  pos5=receitas.find(";",pos4+1)
                  listav.append(receitas[pos1:pos4+1])
                  listanv.append(receitas[pos3+1:pos4])
                  pos=pos5
              a=open("visualizacoes.txt","r",encoding="utf-8")
              le=a.read()
              a.close()
              lista1v=[]
              lis=len(listav)
              for i in range(lis):
                 cont=le.count(listav[i])
                 lista1v.append(cont)
              lista2v=lista1v.copy()
              lista2v.sort()
              lista2v.reverse()
              cont2=len(lista2v)
              lista4v=[]
              for i in range(cont2):
                 ss=lista1v.index(lista2v[i])
                 lista4v.append(str(listav[ss]))  
              lena3=len(lista4v)
              lista5=[]
              for i in range(lena3):
                  posv=lista.index(lista4v[i])
                  lista5.append(lista2[posv])
              l_receitaconj.delete(0,"end")
              for item in lista5:
                  l_receitaconj.insert("end",item)
         def ordernarl():
             f=open("receitas.txt","r",encoding="utf-8")
             receitas=f.read()
             f.close()
             pos=0
             listal=[]
             listanl=[]
             cont=receitas.count(";")
             media=cont/4
             for i in range(int(media)):
                 pos1=receitas.find(";",pos)
                 pos2=receitas.find(";",pos1+1)
                 pos3=receitas.find(";",pos2+1)
                 pos4=receitas.find(";",pos3+1)
                 pos5=receitas.find(";",pos4+1)
                 listal.append(receitas[pos1:pos4+1])
                 listanl.append(receitas[pos3+1:pos4])
                 pos=pos5
             a1=open("likes.txt","r",encoding="utf-8")
             le=a1.read()
             a1.close()
             lista11=[] 
             lis1=len(listal)
             for i in range(lis1):
                 cont=le.count(listal[i])
                 lista11.append(cont)
             lista21=lista11.copy()
             lista21.sort()
             lista21.reverse()
             cont21=len(lista21)
             lista41=[] 
             for i in range(cont21):
                 ss=lista11.index(lista21[i])
                 lista41.append(str(listal[ss]))
                 lena3=len(lista41)
             lista5=[]
             for i in range(lena3):
                 posv=lista.index(lista41[i])
                 lista5.append(lista2[posv])
             l_receitaconj.delete(0,"end")
             for item in lista5:
                 l_receitaconj.insert("end",item)
         def repor():
              f=open("receitas.txt","r",encoding="utf-8")
              receita=f.read()
              f.close()
              pos=0
              cont=receita.count(";")
              media=cont/4
              lista=[]
              lista2=[]
              for i in  range(int(media)+1):
                 pos1=receita.find(";",pos)
                 pos2=receita.find(";",pos1+1)
                 pos3=receita.find(";",pos2+1)
                 pos4=receita.find(";",pos3+1)
                 pos5=receita.find(";",pos4+1)
                 lista.append(receita[pos1:pos4+1])
                 texto=str(i+1)+"."+receita[pos3+1:pos4]
                 lista2.append(texto)
                 pos=pos5    
              lena=len(lista)
              for i in range(lena):
                 if lista[i]=="":
                     del lista[i]
              lena1=len(lista) 
              lena2=len(lista2)
              if lena1!=lena2:
                 del lista2[lena1]
              l_receitaconj.delete(0,"end")
              for item in lista2:
                 l_receitaconj.insert("end",item)
         #Começa aqui...
         window_pa=Toplevel() 
         window_pa.geometry("1500x780")
         window_pa.title("OrganizEat:Catálogo de Receitas:Pesquisa Avançada")
         window_pa.configure(bg="#2785bc")
         lbl_conjunto=LabelFrame(window_pa,text="Catálogo de Receitas",width=1480,height=750,bg="#2785bc",fg="white")
         lbl_conjunto.place(x=10,y=10)
         l_receitaconj=Listbox(lbl_conjunto,width=37,height=21)
         l_receitaconj.place(x=10,y=10)
         l_categoria=Label(lbl_conjunto,text="Categoria:",bg="#2785bc",fg="white")
         l_categoria.place(x=1063,y=10)
         e_categoria=Entry(lbl_conjunto,width=35)
         e_categoria.place(x=1127,y=10)
         l_autor=Label(lbl_conjunto,text="Autor:",bg="#2785bc",fg="white")
         l_autor.place(x=1063,y=40)
         e_autor=Entry(lbl_conjunto,width=35)
         e_autor.place(x=1127,y=40)
         btn_consult4=Button(lbl_conjunto,text="Consultar",width=31,height=3,command=consultar,fg="white",bg="#e0a000")
         btn_consult4.place(x=10,y=360)
         btn_adicionar=Button(lbl_conjunto,text="Adicionar à minha Lista de Favoritas",width=31,height=3,fg="white",bg="#e0a000")
         btn_adicionar.place(x=10,y=420)
         txt_consulta=Text(lbl_conjunto,width=100,height=30)
         txt_consulta.place(x=250,y=10)
         ctn_canas2=Canvas(lbl_conjunto,width=400,height=400,bd=2,relief="sunken")
         ctn_canas2.place(y=87,x=1063)
         lbl_outro4=LabelFrame(lbl_conjunto,width=940,height=220,bg="#2785bc",fg="white",relief="sunken")
         lbl_outro4.place(x=520,y=508)
         lbl_comentarios4=Label(lbl_outro4,text="Comentários:",bg="#2785bc",fg="white")
         lbl_comentarios4.place(x=180,y=10)
         txt_comentarios4=Listbox(lbl_outro4,width=40,height=11,state="disable")
         txt_comentarios4.place(x=180,y=30)
         lbl_ccomentarios4=Label(lbl_outro4,text="Criar Comentário:",bg="#2785bc",fg="white")
         lbl_ccomentarios4.place(x=470,y=10)
         txt_ccomentarios4=Text(lbl_outro4,width=45,height=8,state="disable")
         txt_ccomentarios4.place(x=470,y=30)
         btn_ccomentário4=Button(lbl_outro4,text="Criar Comentário",width=51,state="disable",fg="white",bg="#e0a000")
         btn_ccomentário4.place(x=470,y=170)
         lbl_like4=Label(lbl_outro4,text="Nº. de Likes:",bg="#2785bc",fg="white")
         lbl_like4.place(x=10,y=60)
         txt_like4=Entry(lbl_outro4,width=18)
         txt_like4.place(x=10,y=80)
         btn_like4=Button(lbl_outro4,text="Like",width=15,height=6,state="disable",fg="white",bg="#e0a000")
         btn_like4.place(x=10,y=110)
         lbl_v4=Label(lbl_outro4,text="Nº. de Visualizações:",bg="#2785bc",fg="white")
         lbl_v4.place(x=10,y=10)
         txt_v4=Entry(lbl_outro4,width=18,)
         txt_v4.place(x=10,y=30)
         lbl_frame_filtros=LabelFrame(lbl_conjunto,text="Filtros",width=490,height=227,bg="#2785bc",fg="white",relief="sunken")
         lbl_frame_filtros.place(x=10,y=500)
         filtros=Label(lbl_frame_filtros,text="Pesquisar Ingrediente:",bg="#2785bc",fg="white")
         filtros.place(x=10,y=10)
         entry_filtro=Entry(lbl_frame_filtros,width=55)
         entry_filtro.place(x=135,y=10)
         btn_pesquisar=Button(lbl_frame_filtros,text="PESQUISAR",width=46,command=pesquisar,fg="white",bg="#e0a000")
         btn_pesquisar.place(x=135,y=40)
         cb1=IntVar()
         cb2=IntVar()
         cb3=IntVar()
         cb1_escolha=Checkbutton(lbl_frame_filtros,text="Autor:",variable=cb1,command=filtrar,bg="#2785bc",fg="yellow")
         cb2_escolha=Checkbutton(lbl_frame_filtros,text="Categoria:",variable=cb2,command=filtrar,bg="#2785bc",fg="yellow")
         cb3_escolha=Checkbutton(lbl_frame_filtros,text="Todos os Filtros(Autor e Categoria)",variable=cb3,command=filtrar,bg="#2785bc",fg="yellow")
         cb1_escolha.place(x=10,y=80)
         cb2_escolha.place(x=10,y=120)
         cb3_escolha.place(x=10,y=160)
         l=open("login.txt","r")
         autor=l.read()
         l.close()
         lenaa=autor.count(";")
         mediaa=lenaa/3
         pos=0
         lista_autor=[]
         for i in range(int(mediaa)+1):
             pos1=autor.find(";",pos)
             pos2=autor.find(";",pos1+1)
             pos3=autor.find(";",pos2+1)
             pos4=autor.find(";",pos3+1)
             lista_autor.append(autor[pos1+1:pos2])
             pos=pos4
         lenaa1=len(lista_autor)
         for i in range(lenaa1):
             if lista_autor[i]=="":
                 del lista_autor[i]
         box_filtro1=Combobox(lbl_frame_filtros,width=20,values=lista_autor)
         box_filtro1.place(x=90,y=80)
         a=open("categorias.txt","r")
         categoria=a.read()
         a.close()
         lenac=categoria.count(";")
         pos=0
         listacategoria=[]
         for i in range(lenac):
             pos1=categoria.find(";",pos)
             pos2=categoria.find(";",pos1+1)
             listacategoria.append(categoria[pos1+1:pos2])
             pos=pos2
         lenacc=len(listacategoria)
         for i in range(lenacc):
             if listacategoria[i]=="":
                 del listacategoria[i]
         box_filtro2=Combobox(lbl_frame_filtros,width=20,values=listacategoria)
         box_filtro2.place(x=90,y=120)
         btn_ov=Button(lbl_frame_filtros,text="Ordernar por Visualizações",width=20,command=ordernarv,fg="white",bg="#e0a000")
         btn_ov.place(x=290,y=80)
         btn_ol=Button(lbl_frame_filtros,text="Ordernar por Likes",width=20,command=ordernarl,fg="white",bg="#e0a000")
         btn_ol.place(x=290,y=120)
         btn_repor=Button(lbl_frame_filtros,text="Repor Catálogo",width=20,command=repor,fg="white",bg="#e0a000")
         btn_repor.place(x=290,y=160)
         f=open("receitas.txt","r",encoding="utf-8")
         receita=f.read()
         f.close()
         pos=0
         cont=receita.count(";")
         media=cont/4
         lista=[]
         lista2=[]
         for i in  range(int(media)+1):
              pos1=receita.find(";",pos)
              pos2=receita.find(";",pos1+1)
              pos3=receita.find(";",pos2+1)
              pos4=receita.find(";",pos3+1)
              pos5=receita.find(";",pos4+1)
              lista.append(receita[pos1:pos4+1])
              texto=str(i+1)+"."+receita[pos3+1:pos4]
              lista2.append(texto)
              pos=pos5    
         lena=len(lista)
         for i in range(lena):
             if lista[i]=="":
                 del lista[i]
         lena1=len(lista) 
         lena2=len(lista2)
         if lena1!=lena2:
             del lista2[lena1]
         for item in lista2:
             l_receitaconj.insert("end",item)
         window_pa.mainloop()
     def tomr():
         window_tomr=Toplevel()
         window_tomr.geometry("710x320")
         window_tomr.title("OrganizEat:Top of Most Rated")
         window_tomr.configure(bg="#2785bc")
         l_tof=Label(window_tomr,text="Top of Most Rated",bg="#2785bc",fg="white")
         l_tof.place(x=10,y=10)
         lbl1=LabelFrame(window_tomr,text="Por visualizações:",width=320,height=263,relief="sunken",bg="#2785bc",fg="white")
         lbl1.place(x=10,y=40)
         tree=ttk.Treeview(lbl1,columns=("Receita","Visualizações"),show="headings")
         tree.column("Receita",anchor="c",width=200)
         tree.column("Visualizações",anchor="c",width=100)
         tree.heading("Receita",text="Receita:")
         tree.heading("Visualizações",text="Visualizações:")
         tree.place(x=5,y=5)
         lbl2=LabelFrame(window_tomr,text="Por Likes:",width=320,height=263,relief="sunken",bg="#2785bc",fg="white")
         lbl2.place(x=380,y=40)
         tree2=ttk.Treeview(lbl2,columns=("Receita","Likes"),show="headings")
         tree2.column("Receita",anchor="c",width=200)
         tree2.column("Likes",anchor="c",width=100)
         tree2.heading("Receita",text="Receita:")
         tree2.heading("Likes",text="Likes:")
         tree2.place(x=5,y=5)
         f=open("receitas.txt","r",encoding="utf-8")
         receitas=f.read()
         f.close()
         pos=0
         lista=[]
         listan=[]
         cont=receitas.count(";")
         media=cont/4
         for i in range(int(media)):
             pos1=receitas.find(";",pos)
             pos2=receitas.find(";",pos1+1)
             pos3=receitas.find(";",pos2+1)
             pos4=receitas.find(";",pos3+1)
             pos5=receitas.find(";",pos4+1)
             lista.append(receitas[pos1:pos4+1])
             listan.append(receitas[pos3+1:pos4])
             pos=pos5
         f=open("receitas.txt","r",encoding="utf-8")
         receitas=f.read()
         f.close()
         pos=0
         lista=[]
         listan=[]
         cont=receitas.count(";")
         media=cont/4
         for i in range(int(media)):
             pos1=receitas.find(";",pos)
             pos2=receitas.find(";",pos1+1)
             pos3=receitas.find(";",pos2+1)
             pos4=receitas.find(";",pos3+1)
             pos5=receitas.find(";",pos4+1)
             lista.append(receitas[pos1:pos4+1])
             listan.append(receitas[pos3+1:pos4])
             pos=pos5
         a=open("visualizacoes.txt","r",encoding="utf-8")
         le=a.read()
         a.close()
         lista1=[]
         lis=len(lista)
         for i in range(lis):
             cont=le.count(lista[i])
             lista1.append(cont)
             lista2=lista1.copy()
             lista2.sort()
             lista2.reverse()
         cont2=len(lista2)
         lista4=[]
         for i in range(cont2):
             ss=lista1.index(lista2[i])
             lista4.append(str(listan[ss]))
             lista4.append(str(lista2[i]))
         lena1=len(lista4)/2
         poss=0
         poss1=1
         for i in range(int(lena1)):
             tree.insert("","end",values=(lista4[poss],lista4[poss1]))
             poss=poss+2
             poss1=poss1+2
         a1=open("likes.txt","r",encoding="utf-8")
         le=a1.read()
         a1.close()
         lista11=[] 
         lis1=len(lista)
         for i in range(lis1):
             cont=le.count(lista[i])
             lista11.append(cont)
         lista21=lista11.copy()
         lista21.sort()
         lista21.reverse()
         cont21=len(lista21)
         lista41=[]
         for i in range(cont21):
             ss=lista11.index(lista21[i])
             lista41.append(str(listan[ss]))
             lista41.append(str(lista21[i]))
         lena2=len(lista41)/2
         posss=0
         posss1=1    
         for i in range(int(lena2)):
             tree2.insert("","end",values=(lista41[posss],lista41[posss1]))
             posss=posss+2
             posss1=posss1+2
         window_tomr.mainloop()
     def sair():
         window1.destroy()
     barra_Menu=Menu(window1)
     #Opções de inicio
     simuladores_Menu=Menu(barra_Menu)
     simuladores_Menu.add_command(label="Ajuda")
     simuladores_Menu.add_command(label="Sair",command=sair)
     barra_Menu.add_cascade(label="Inicio",menu=simuladores_Menu)
     cr_Menu=Menu(barra_Menu)
     cr_Menu.add_command(label="Top of Most Rated",command=tomr)
     cr_Menu.add_command(label="Pesquisa Avançada",command=pesquisaavancada)
     barra_Menu.add_cascade(label="Catálogo de Receitas",menu=cr_Menu)
     window1.configure(menu=barra_Menu)
     
     #Conteudo Página Principal
     
     
     
     window1.mainloop() 

#Janela Criar_Conta
def criarconta():
    def limpar():
        txt_cuser.delete(0,"end")
        txt_ccpassword.delete(0,"end")
        txt_cpassword.delete(0,"end")
        txt_cemail.delete(0,"end")
    def criar():
        texto=txt_cuser.get()+";"+txt_cpassword.get()+";"+txt_cemail.get()+";"
        texto1=txt_cuser.get()
        texto2=txt_cpassword.get()
        texto3=txt_cemail.get()
        texto4=txt_ccpassword.get()
        f=open("login.txt","r")
        for linha in f:
            login_c=str(linha)
        f.close() 
        pos1=login_c.find(texto)
        pos2=login_c.find(texto1)
        pos3=login_c.find(texto2)
        pos4=login_c.find(texto3)
        pos5=texto4.find(texto2)
        if pos5!=-1:
              if pos1!=-1 and pos2!=-1 and pos3!=-1 and pos4!=-1:
                 messagebox.showerror("Erro","Credencial(ais) já existe(m). ")
              else:
                 f=open("login.txt","a")
                 f.write(texto)
                 f.close()
                 messagebox.showinfo("Informação","A conta foi criada com sucesso!!")
                 window_cc.destroy()
        else:
            messagebox.showerror("Erro","As passwords não coincidem.") 
    window_cc=Tk()
    window_cc.geometry("500x300")
    window_cc.title("OrganizEat:Criar Conta")
    window_cc.configure(bg="#2785bc")
    frame2=LabelFrame(window_cc,text="Criar Conta",width=450,height=250,relief="sunken",bg="#2785bc",fg="white")
    frame2.place(x=25,y=20)
    lbl_cuser=Label(frame2,text="Username:",fg="white",bg="#2785bc")
    txt_cuser=Entry(frame2,width=40)
    txt_cuser.place(x=97,y=30)
    lbl_cuser.place(x=10,y=30)
    lbl_cpassword=Label(frame2,text="Password:",fg="white",bg="#2785bc")
    lbl_cpassword.place(x=10,y=70)
    txt_cpassword=Entry(frame2,width=40,show="*")
    txt_cpassword.place(x=97,y=70)
    lbl_ccpassword=Label(frame2,text="Conf.Password:",fg="white",bg="#2785bc")
    lbl_ccpassword.place(x=10,y=110)
    txt_ccpassword=Entry(frame2,width=40,show="*")
    txt_ccpassword.place(x=97,y=110)
    lbl_cemail=Label(frame2,text="Email:",fg="white",bg="#2785bc")
    lbl_cemail.place(x=10,y=150)
    txt_cemail=Entry(frame2,width=40)
    txt_cemail.place(x=97,y=150)
    btn_limpar=Button(frame2,text="Limpar",width=15,fg="white",command=limpar,bg="#e0a000")
    btn_limpar.place(x=170,y=190)
    btn_criar=Button(frame2,text="Criar",width=15,fg="white",command=criar,bg="#e0a000")
    btn_criar.place(x=310,y=190) 
    window_cc.mainloop()

#Janlea Login
window=Tk()
window.geometry("600x500")
window.title("OrganizEat:Login")
bg=PhotoImage(file="fundologin2.gif")
labelfundo=Label(window,image=bg)
labelfundo.place(x=0,y=0,relwidth=1,relheight=1)
def limpar1():
    txt_user.delete(0,"end")
    txt_email.delete(0,"end")
    txt_password.delete(0,"end")
def ajuda():
    wb.open("Manual de Utilizador_OrganizEat.pdf")
frame1=LabelFrame(window,fg="white",text="LOGIN",width=550, height=200,relief="sunken")
frame1.config(bg="#2785bc")
frame1.place(x=25,y=280)
lbl_user=Label(frame1, text="Username:",bg="#2785bc",fg="white") #falta escolher a fonte, tamanho da letra
lbl_user.place(x=20,y=30)
user=StringVar()
txt_user=Entry(frame1,width=20,textvariable=user)
txt_user.place(x=86,y=30)
lbl_password=Label(frame1,text="Password:",bg="#2785bc",fg="white")#encontra-se em falta os mesmo itens relativos a lbl_user
lbl_password.place(x=20,y=70)
txt_password=Entry(frame1,width=20,show="*")
txt_password.place(x=86,y=70)
lbl_email=Label(frame1,text="Email:",bg="#2785bc",fg="white")
lbl_email.place(x=20,y=110)
txt_email=Entry(frame1,width=20)
txt_email.place(x=86,y=110)
btn=Button(frame1, bg="#e0a000",fg="white",text="Login",width=16,command=lambda:paginainicial(user))
btn.place(x=86,y=140)
btn_ajuda=Button(frame1,bg="#e0a000",fg="white",text="AJUDA",width=20,command=ajuda)
btn_ajuda.place(x=316,y=10)
btn_cc=Button(frame1,bg="#e0a000",fg="white",text="CRIAR CONTA",width=20,command=criarconta)
btn_cc.place(x=316,y=50)
btn_rc=Button(frame1,text="LIMPAR",bg="#e0a000",fg="white",width=20,command=limpar1)
btn_rc.place(x=316,y=90)
btn_ma=Button(frame1,text="MODO ANÓNIMO",bg="#e0a000",fg="white",width=20,command=lambda:modoanonimo(user))
btn_ma.place(x=316,y=130)

window.mainloop()