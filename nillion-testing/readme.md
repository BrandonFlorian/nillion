# Nillion Experiments

A repository for exploring and testing various Nillion programs and features. Created using the Nillion quickstart template.

## Structure

This project contains:

- A Next.js frontend in `app/`
- Nillion programs in `nada/`

## Programs

### Current Programs:

1. **Millionaires Problem** - A classic MPC example that determines the highest value among participants without revealing individual values
   - Located in `nada/millionaires/`
   - Uses secure multi-party computation to compare values privately

### Setup

1. Install dependencies:

```bash
# Install frontend dependencies
cd frontend
npm install

# Install Nillion CLI if you haven't already
curl -L https://raw.githubusercontent.com/nillion-oss/nillion-cli/main/install.sh | bash

# Setup Nillion devnet
nillion-devnet setup
```

2. Start the development server:

```bash
# Start the frontend
cd frontend
npm run dev
```

3. Run Nillion programs:

```bash
# From the nada directory
cd nada
python3 your_program.py
```

## Development

This repository serves as a playground for testing various Nillion features and programs. Each program will be organized in its own directory under `nada/` with its own documentation.

## Environment Variables

Make sure to set up your environment variables:

- Copy `.env.example` to `.env`
- Fill in the necessary Nillion credentials (these are automatically populated when you run `nillion-devnet setup`)

## Testing

Each program includes its own test suite. To run tests:

```bash
cd nada
python -m pytest
```

## Contributing

Feel free to add your own experiments and programs! Just create a new directory under `nada/` for each new program.

## Resources

- [Nillion Documentation](https://docs.nillion.com/)
- [Next.js Documentation](https://nextjs.org/docs)
- [Nillion Discord](https://discord.gg/nillion)

## License

MIT
