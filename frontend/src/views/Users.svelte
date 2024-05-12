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
    <div class="tableWrap">
        <table>
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Email</th>
                    <th>Login</th>
                    <th>Created date</th>
                    <th>Is superuser</th>
                    <th>Is banned</th>
                </tr>
            </thead>
            <tbody>
                {#each users as user}
                    <tr>
                        <td><div>{user.userId}</div></td>
                        <td>{user.email}</td>
                        <td>{user.nickname}</td>
                        <td>{user.created}</td>
                        <td>{user.isSuperUser}</td>
                        <td>{user.isBanned}</td>
                    </tr>
                {/each}
            </tbody>
        </table>
    </div>
</div>

<style lang="scss">
    .tableWrap {
        height: 400px;
        border: 2px solid black;
        overflow: auto;
    }

    thead tr th {
    position: sticky;
    top: 0;
    }

    table {
        border-collapse: collapse;
    }

    th {
        padding: 16px;
        padding-left: 15px;
        border-left: 1px dotted rgba(200, 209, 224, 0.6);
        border-bottom: 1px solid #e8e8e8;
        background: #ffc491;
        text-align: left;
    
        box-shadow: 0px 0px 0 2px #e8e8e8;
    }


    table {
        width: 100%;
        font-family: sans-serif;
    }

    table td {
        padding: 16px;
    }
    
    tbody tr {
        border-bottom: 2px solid #e8e8e8;
    }
    
    thead {
        font-weight: 500;
        color: rgba(0, 0, 0, 0.85);
    }
    
    tbody tr:hover {
        background: #e6f7ff;
    }
</style>