from interfaz.inicio_de_sesion import LoginBocaHandball

if __name__ == "__main__":
    app = LoginBocaHandball()
    app.mainloop()


if __name__ == "__main__":
    try:
        app.mainloop()
    except KeyboardInterrupt:
        print("\nAplicación cerrada por el usuario.")