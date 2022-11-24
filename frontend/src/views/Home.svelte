<script lang="ts">
    import { Link } from 'svelte-routing';

    export let location;
    const noop = location;
</script>

<div>
    <h1 class="testStyle">Home page</h1>
</div>

<style lang="scss">
    .testStyle {
        color: tomato
    }
</style>