def define_env(env):

    @env.macro
    def test():
        return "Hello World!"
