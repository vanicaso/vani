import glfw


def main():
    # Inicializando la libreria GLFW
    if not glfw.init():
        return -1
    # Creamos una ventana
    window = glfw.create_window(720, 600, "Python GLFW", None, None)
    if not window:
        glfw.terminate()
        return -1
    # Actualiza el contexto de la ventana
    glfw.make_context_current(window)
    # Bucle infinito, se para cuado el usuario cierra la ventana
    while not glfw.window_should_close(window):
        # Codigo OpenGL para renderizar
        # Cambia los buffer delantero y traseros
        glfw.swap_buffers(window)
        # Esperado eventos
        glfw.poll_events()
    # Cierra la bibioteca
    glfw.terminate()


if __name__ == "__main__":
    main()
