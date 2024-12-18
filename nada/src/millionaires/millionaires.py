import asyncio
import os
import pytest

from nillion_client import (
    Network,
    NilChainPayer,
    NilChainPrivateKey,
    VmClient,
    PrivateKey,
)
from dotenv import load_dotenv

from config import CONFIG_PARTY_1

home = os.getenv("HOME")
load_dotenv(f"{home}/.config/nillion/nillion-devnet.env")


# Alice stores the millionaires program in the network
async def main():
    # Use the devnet configuration generated by `nillion-devnet`
    network = Network.from_config("devnet")

    # Create payments config and set up Nillion wallet with a private key to pay for operations
    nilchain_key: str = os.getenv("NILLION_NILCHAIN_PRIVATE_KEY_0")  # type: ignore
    payer = NilChainPayer(
        network,
        wallet_private_key=NilChainPrivateKey(bytes.fromhex(nilchain_key)),
        gas_limit=10000000,
    )
    signing_key = PrivateKey(CONFIG_PARTY_1["private_key"])
    client = await VmClient.create(signing_key, network, payer)

    # Adding funds to the client balance so the upcoming operations can be paid for
    funds_amount = 1000
    print(f"💰  Adding some funds to the client balance: {funds_amount} uNIL")
    await client.add_funds(funds_amount)

    # Store millionaires program in the network
    millionaires_program_name = "millionaires"
    program_mir_path = f"../nada_programs/target/{millionaires_program_name}.nada.bin"
    print(f"Storing program in the network: {millionaires_program_name}")
    program = open(program_mir_path, "rb").read()
    program_id = await client.store_program(millionaires_program_name, program).invoke()

    user_id_alice = client.user_id

    print(f"Alice stores millionaires program at program_id: {program_id}")
    print("Alice tells Bob and Charlie her user_id and the millionaires program_id")

    print(
        "\n📋⬇️ Copy and run the following command to store Bob and Charlie's salaries in the network"
    )
    print(
        f"\npython3 02_store_secret_party_n.py --user_id_1 {user_id_alice} --program_id {program_id}"
    )
    return [user_id_alice, program_id]


if __name__ == "__main__":
    asyncio.run(main())


@pytest.mark.asyncio
async def test_main():
    pass