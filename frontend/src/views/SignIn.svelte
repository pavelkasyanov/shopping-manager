<script lang="ts">
    import { login } from 'src/store/session.service';
    import { navigate } from 'svelte-routing';
    import { prevent_default } from 'svelte/internal';

    export let location;
    const noop = location;

    let username: string = null;
    let passwd: string = null;

    const signin = async () => {
        if (!username || !passwd) {
            alert('invalid login or password!');
            return;
        }

        const result = await login(username, passwd);
        debugger
        if (result) {
            navigate('/home')
        }

    }

</script>

<div class="formContainer">
    <form>
        <div>
            <label for="login">Login</label>
            <input id="login" bind:value={username} />
        </div>
        <div>
            <label for="password">password</label>
            <input id="password"  type="password" bind:value={passwd} />
        </div>
        <input type="submit" class="singInBtn" on:click|preventDefault={signin} content="signin" />
    </form>
</div>

<style lang="scss">

    form {
        display: table-caption;
    }

    .formContainer {
        position:absolute;
        top:50%;
        left:40%;
    }

    .singInBtn {
        margin-top: 10px;
    }
</style>