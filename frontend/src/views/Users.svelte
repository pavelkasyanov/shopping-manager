<script lang="ts">
    import { onMount } from 'svelte';
    import { getAllUsers } from 'src/services/apiService';

    let users = [];

    onMount(async () => {
        users = await getAllUsers();
    });

</script>

<div>
    <h1 class="testStyle">Users</h1>
    <table>
        <tr>
            <th>Id</th>
            <th>Email</th>
            <th>Login</th>
            <th>Created date</th>
            <th>Is superuser</th>
            <th>Is banned</th>
        </tr>
        <tr>
            {#each users as user}
                <td>{user.userId}</td>
                <td>{user.email}</td>
                <td>{user.nickname}</td>
                <td>{user.created}</td>
                <td>{user.isSuperUser}</td>
                <td>{user.isBanned}</td>
            {/each}
        </tr>
    </table>
</div>

<style lang="scss">
    table {
        border: 4px double black;
        width: 100%;
        height: 90%;
    }
    td {
        text-align: center;
    }
</style>